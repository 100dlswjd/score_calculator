import sqlite3

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

def commit():
    conn.commit()

def close():
    conn.close()
    
def add_member(name):
    cur.execute(f"alter table {table_name} add {name} int default null")