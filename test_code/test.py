import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("SELECT data, data2, data3, data4, data5 FROM test")
rows = cursor.fetchall()

cumulative_data = {}

for row in rows:
    data1, data2, data3, data4, data5 = row

    pattern = tuple(col is not None for col in row)

    if pattern not in cumulative_data:
        cumulative_data[pattern] = {
            'cumulative_values': [0, 0, 0, 0, 0],  # Initialize with zeros for each data column
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
