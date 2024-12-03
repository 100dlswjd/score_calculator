import sqlite3

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
sql = sql[:-2] + " FROM test"

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

for pattern, data in cumulative_data.items():
    print(f"Pattern {pattern}:")
    print(f"  Count: {data['count']}")
    print(f"  Cumulative values: {data['cumulative_values']}")

conn.close()
