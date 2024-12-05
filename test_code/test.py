import sqlite3
import os
from collections import defaultdict
from datetime import datetime

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

sql = "SELECT REG_DATE, "
for name in names:
    sql += f"{name}, "
sql = sql[:-2] + f" FROM {table_name} where SITE = 1"

cur.execute(sql)
rows = cur.fetchall()

cumulative_data = defaultdict(lambda: defaultdict(lambda: { 'cumulative_values': [0 for _ in range(len(names))], 'count': 0 }))

# Accumulate values by date and pattern
for row in rows:
    date = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').date()
    data_values = row[1:]
    pattern = tuple(col is not None for col in data_values)

    cumulative_data[date][pattern]['count'] += 1
    for i, value in enumerate(data_values):
        if value is not None:
            cumulative_data[date][pattern]['cumulative_values'][i] += value

# Generate output
res = ""
for date, patterns in cumulative_data.items():
    formatted_date = date.strftime('%y.%m.%d (%a)')
    res += f"{formatted_date} Roll 결과\n"
    for pattern, data in patterns.items():
        participant_names = [names[i] for i, value in enumerate(pattern) if value]
        res += "\n"
        res += f"-- {', '.join(participant_names)} --\n"
        cumulative_scores = [f"{names[i]} {data['cumulative_values'][i]} 점" for i, value in enumerate(pattern) if value]
        res += f"{', '.join(cumulative_scores)}\n"
    res += "------------------------------\n"

print(res)
conn.close()
