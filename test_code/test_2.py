import sqlite3
from itertools import combinations

# Connect to your database
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# 컬럼이름 가져와서 sql문으로 만들기
cur.execute("PRAGMA table_info(test)")
rows = cur.fetchall()
names = []
for row in rows:
    names.append(row[1])
names = names[3:]

sql = "SELECT "
for name in names:
    sql += f"{name}, "
sql = sql[:-2] + " FROM test where SITE = 1"

# Step 1: Query all rows and retrieve the column names
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
    
    cumulative_sums[pair_key] = {'cumulative1': 0, 'cumulative2': 0, 'valid': False}

    # Step 4: Accumulate values for the current pair if both are non-null
    for row in rows:
        value1, value2 = row[col1], row[col2]

        if value1 is not None and value2 is not None:
            cumulative_sums[pair_key]['cumulative1'] += value1
            cumulative_sums[pair_key]['cumulative2'] += value2
            cumulative_sums[pair_key]['valid'] = True

current_col1 = None
# Step 5: Print cumulative values for each valid pair
for pair, cumulative_value in cumulative_sums.items():
    
    col1 = pair.split('_')[0]
    if current_col1 is None or current_col1 != col1:
        print(f"============== {col1} ==============")
        current_col1 = col1
        
    if cumulative_value['valid']:
        print(f"역대 전적 {pair}: {str(pair).split('_')[0]} = {cumulative_value['cumulative1']}, {str(pair).split('_')[1]} = {cumulative_value['cumulative2']}")
    else:
        print(f"전적 결과 없음 {pair}")

# Close the connection
conn.close()
