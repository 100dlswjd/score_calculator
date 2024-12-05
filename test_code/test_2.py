import sqlite3
import os
from itertools import combinations

config_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","scoreboard","config.json")

table_name = "score"
db_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","scoreboard",f"{table_name}.db")

# Connect to your database
conn = sqlite3.connect(db_path)

cur = conn.cursor()
cur.execute(f"PRAGMA table_info({table_name})")
rows = cur.fetchall()
names = []
for row in rows:
    names.append(row[1])
names = names[3:]

# Step 1: Query all rows and retrieve the column names
sql = "SELECT "
for name in names:
    sql += f"{name}, "
sql = sql[:-2] + f" FROM {table_name} where SITE = 1"

cur.execute(sql)
rows = cur.fetchall()
# Get the column names from the cursor
column_names = [description[0] for description in cur.description]

# Step 2: Create a dictionary to track cumulative sums for each pair of columns
cumulative_sums = {}

# Step 3: Iterate through each possible pair of columns by name
num_columns = len(column_names)  # Number of columns
for col1, col2 in combinations(range(num_columns), 2):
    col_name1 = column_names[col1]
    col_name2 = column_names[col2]
    pair_key = f"{col_name1}_{col_name2}"
    reverse_pair_key = f"{col_name2}_{col_name1}"

    cumulative_sums[pair_key] = {'cumulative1': 0, 'cumulative2': 0, 'valid': False, 'total_games': 0}

    # Step 4: Accumulate values for the current pair if both are non-null
    for row in rows:
        value1, value2 = row[col1], row[col2]

        if value1 is not None and value2 is not None:
            cumulative_sums[pair_key]['cumulative1'] += value1
            cumulative_sums[pair_key]['cumulative2'] += value2
            cumulative_sums[pair_key]['total_games'] += 1
            cumulative_sums[pair_key]['valid'] = True

    # Ensure the reverse pair also has the same values for consistent output
    cumulative_sums[reverse_pair_key] = {
        'cumulative1': cumulative_sums[pair_key]['cumulative2'],
        'cumulative2': cumulative_sums[pair_key]['cumulative1'],
        'valid': cumulative_sums[pair_key]['valid'],
        'total_games': cumulative_sums[pair_key]['total_games']
    }

# Step 5: Print cumulative values for each valid pair, ensuring each pair appears under both columns
res = ""
printed_pairs = set()
for col1 in range(num_columns):
    col_name1 = column_names[col1]
    res += f"=======  {col_name1}  =======\n"
    for col2 in range(num_columns):
        if col1 != col2:
            col_name2 = column_names[col2]
            pair_key = f"{col_name1}_{col_name2}"

            if pair_key in cumulative_sums and pair_key not in printed_pairs:
                cumulative_value = cumulative_sums[pair_key]
                if cumulative_value['valid']:
                    res += f"{col_name1} = {cumulative_value['cumulative1']} / {col_name2} = {cumulative_value['cumulative2']} (총 판수: {cumulative_value['total_games']}) "
                    if cumulative_value['cumulative1'] > cumulative_value['cumulative2']:
                        res += "승\n"
                    elif cumulative_value['cumulative1'] < cumulative_value['cumulative2']:
                        res += "패\n"
                    else:
                        res += "무\n"
                else:
                    res += f"{col_name1}과 {col_name2}의 전적이 없음.\n"
                printed_pairs.add(pair_key)
    res += "=====================\n"

print(res)

conn.close()