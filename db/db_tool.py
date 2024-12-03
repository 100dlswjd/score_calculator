import sqlite3
from itertools import combinations

table_name = "score"

conn = sqlite3.connect(f'{table_name}.db')
cur = conn.cursor()

try:
    cur.execute(f'''create table {table_name} (IDX integer primary key, SITE integer not null, REG_DATE date)''')
except:
    pass

def getnames():
    cur.execute(f"PRAGMA table_info({table_name})")
    rows = cur.fetchall()
    names = []
    for row in rows:
        names.append(row[1])
    names = names[3:]
    return names

def get_total_score(site):
    sql = sql = "SELECT "
    names = getnames()
    for name in names:
        sql += f"{name}, "
    sql = sql[:-2] + f" FROM {table_name} where SITE = {site}"
    
    cur.execute(sql)
    rows = cur.fetchall()
    
    cumulative_data = {}
    
    for row in rows:
        pattern = tuple(col is not None for col in row)
        
        if pattern not in cumulative_data:
            cumulative_data[pattern] = {
                'cumulative_values': [0 for x in range(len(names))],  # Initialize with zeros for each data column
                'count': 0  # Initialize counter to 0
            }

        cumulative_data[pattern]['count'] += 1
        for i, value in enumerate(row):
            if value is not None:
                cumulative_data[pattern]['cumulative_values'][i] += value

    res = ""
    for pattern, data in cumulative_data.items():
        # print(f"Pattern {pattern}:")
        # print(f"  Count: {data['count']}")
        # print(f"  Cumulative values: {data['cumulative_values']}")
        # for i, value in enumerate(pattern):
        #     if value:
        #         res += f"{names[i]}: {data['cumulative_values'][i]}\n"
        # pattern에 해당하는 컬럼명 가져와서 데이터 출력 False라면 출력 안함
        res += "----------------------------------\n"
        for i, value in enumerate(pattern):
            if value:
                res += f"{names[i]}: {data['cumulative_values'][i]}\n"
        res += "----------------------------------\n"
        
    return res

def get_1_1_score(site):
    names = getnames()
    sql = "SELECT "
    for name in names:
        sql += f"{name}, "
    sql = sql[:-2] + f" FROM {table_name} where SITE = " + str(site)

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
        
        cumulative_sums[pair_key] = {'cumulative1': 0, 'cumulative2': 0, 'valid': False}

        # Step 4: Accumulate values for the current pair if both are non-null
        for row in rows:
            value1, value2 = row[col1], row[col2]

            if value1 is not None and value2 is not None:
                cumulative_sums[pair_key]['cumulative1'] += value1
                cumulative_sums[pair_key]['cumulative2'] += value2
                cumulative_sums[pair_key]['valid'] = True

        # Ensure the reverse pair also has the same values for consistent output
        cumulative_sums[reverse_pair_key] = {
            'cumulative1': cumulative_sums[pair_key]['cumulative2'],
            'cumulative2': cumulative_sums[pair_key]['cumulative1'],
            'valid': cumulative_sums[pair_key]['valid']
        }

    # Step 5: Print cumulative values for each valid pair, ensuring each pair appears under both columns
    res = ""
    printed_pairs = set()
    for col1 in range(num_columns):
        col_name1 = column_names[col1]
        res += f"=======================  {col_name1}  =======================\n"
        for col2 in range(num_columns):
            if col1 != col2:
                col_name2 = column_names[col2]
                pair_key = f"{col_name1}_{col_name2}"

                if pair_key in cumulative_sums and pair_key not in printed_pairs:
                    cumulative_value = cumulative_sums[pair_key]
                    if cumulative_value['valid']:
                        res += f"{col_name1} = {cumulative_value['cumulative1']} / {col_name2} = {cumulative_value['cumulative2']} "
                        if cumulative_value['cumulative1'] > cumulative_value['cumulative2']:
                            res += "승\n"
                        elif cumulative_value['cumulative1'] < cumulative_value['cumulative2']:
                            res += "패\n"
                        else:
                            res += "무\n"
                    else:
                        # print(f"{col_name1}과 {col_name2}의 전적이 없음.")
                        res += f"{col_name1} vs {col_name2}의 전적이 없음.\n"
                    printed_pairs.add(pair_key)
        res += "===============================================================\n"
        
    return res
        
def insert(query):
    cur.execute(query)
    conn.commit()

def add_member(name):
    cur.execute(f"alter table {table_name} add {name} int default null")

def close():
    conn.close()
    
# print(get_total_score(1) + get_1_1_score(1))

# close()