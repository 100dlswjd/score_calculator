import sqlite3
import os

config_path = os.path.join(os.path.expandvars("%userprofile%"), "documents", "ddatg", "scoreboard", "config.json")

table_name = "score"
db_path = os.path.join(os.path.expandvars("%userprofile%"), "documents", "ddatg", "scoreboard", f"{table_name}.db")

# Connect to your database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 컬럼이름 가져와서 sql문으로 만들기
cur.execute(f"PRAGMA table_info({table_name})")
rows = cur.fetchall()

names = []
for row in rows:
    names.append(row[1])
names = names[3:]

sql = "SELECT "
for name in names:
    sql += f"{name}, "
sql = sql[:-2] + f" FROM {table_name} where SITE = 1"

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
    participant_names = [names[i] for i, value in enumerate(pattern) if value]
    res += "-----\n"
    res += f"{' / '.join(participant_names)} -> 총 전적: {data['count']} 판\n"
    for i, value in enumerate(pattern):
        if value:
            res += f"{names[i]}: {data['cumulative_values'][i]}\n"
    res += "-----\n"

print(res)
conn.close()