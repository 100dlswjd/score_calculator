import sqlite3
import os
from itertools import combinations
from collections import defaultdict
from datetime import datetime

# 폴더가 없으면 생성
os.makedirs(os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","scoreboard"), exist_ok=True)

table_name = "score"

db_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","scoreboard",f"{table_name}.db")

conn = sqlite3.connect(db_path)
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

def get_total_score(site, site_name):
    sql = sql = "SELECT "
    names = getnames()
    sql = "SELECT REG_DATE, "
    for name in names:
        sql += f"{name}, "
    sql = sql[:-2] + f" FROM {table_name} where SITE = {site}"

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
        res += f"{formatted_date} {site_name} 결과\n"
        for pattern, data in patterns.items():
            participant_names = [names[i] for i, value in enumerate(pattern) if value]
            res += "\n"
            res += f"-- {', '.join(participant_names)} --\n"
            cumulative_scores = [f"{names[i]} {data['cumulative_values'][i]} 점" for i, value in enumerate(pattern) if value]
            res += f"{', '.join(cumulative_scores)}\n"
        res += "------------------------------\n"

    return res

def get_1_1_score(site, site_name):
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
    individual_win_rates = {name: {'wins': 0, 'total_games': 0} for name in column_names}  # Track wins and total games for each individual
    res += f"\n======= 1:1 전적 ({site_name}) =======\n"
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
                            individual_win_rates[col_name1]['wins'] += 1
                        elif cumulative_value['cumulative1'] < cumulative_value['cumulative2']:
                            res += "패\n"
                            individual_win_rates[col_name2]['wins'] += 1
                        else:
                            res += "무\n"

                        individual_win_rates[col_name1]['total_games'] += 1
                        individual_win_rates[col_name2]['total_games'] += 1
                    else:
                        res += f"{col_name1}과 {col_name2}의 전적이 없음.\n"
                    printed_pairs.add(pair_key)
        res += "=====================\n"

    # Step 6: Calculate win rates and sort participants
    win_rates = []
    for name, data in individual_win_rates.items():
        total_games = data['total_games']
        if total_games > 0:
            win_rate = (data['wins'] / total_games) * 100
        else:
            win_rate = 0
        win_rates.append((name, win_rate))

    win_rates.sort(key=lambda x: x[1], reverse=True)

    # Step 7: Print the final win rate ranking
    res += f"\n======= 최종 승률 순위({site_name}) =======\n"
    for idx, (name, win_rate) in enumerate(win_rates, start=1):
        res += f"{idx}. {name} - {win_rate:.1f}%\n"

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