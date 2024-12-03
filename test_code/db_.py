import sqlite3
import datetime
import time

# DB연결 없으면 생성
con = sqlite3.connect('test.db')

cur = con.cursor()

# 테이블 생성
# cur.execute('''create table test (IDX integer primary key, SITE integer not null, REG_DATE date)''')

# 현재 날짜
# for x in range(10):
    # time.sleep(1)
    # now = datetime.datetime.now()
    # print(now)
    # cur.execute(f"insert into test (SITE, REG_DATE) values ( 1, datetime('{now}'))")


# 컬럼 추가
# cur.execute(f"alter table test add data int default null")
# cur.execute(f"alter table test add data2 int default null")
# cur.execute(f"alter table test add data3 int default null")
# cur.execute(f"alter table test add data4 int default null")
# cur.execute(f"alter table test add data5 int default null")
# cur.execute(f"alter table test add 한글 int default null")


# 컬럼 리스트 가져오기
cur.execute("PRAGMA table_info(test)")
rows = cur.fetchall()
names = []
for row in rows:
    names.append(row[1])
names = names[3:]
print(names)

# 데이터 가져오기
cur.execute("select * from test")
rows = cur.fetchall()
my = 0

get_list = []

for row in rows:
    row = row[3:]
    get_list.append(row)
    
# 0번 인덱스와 1번인덱스가 둘다 None이 아닌경우
for i in range(len(get_list)):
    if get_list[i][0] != None and get_list[i][1] != None:
        print(get_list[i])
        
    


con.commit()

con.close()