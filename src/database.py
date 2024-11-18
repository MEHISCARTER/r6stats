import sqlite3
from datetime import datetime

"""
Concept

MEHISCARTER - Match
ID = M(row number)

| match_id | date | map | result |
----------------------------------

MEHISCARTER - Rounds
ID = match_id-00 (eg; M12-02, Match 12 in the database, round 2 in the match), based on round_num
| round_id | match_id | round_num | result |
--------------------------------------------

MEHISCARTER - UserID
ID = S(row_number)
| stat_id | round_id | Operator | Kills | Deaths | Assists | Site | Side | Result type |
----------------------------------------------------------------------------------------
"""
conn = sqlite3.connect('stats.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Match (
match_id INTEGER PRIMARY KEY,
date TEXT NOT NULL,
map TEXT NOT NULL,
result TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Round (
round_id TEXT PRIMARY KEY,
match_id INTEGER NOT NULL,
round_number INTEGER NOT NULL,
result TEXT NOT NULL,
FOREIGN KEY (match_id) REFERENCES Match (match_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS UserStats (
stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
round_id TEXT NOT NULL,
operator TEXT NOT NULL,
kills INTEGER DEFAULT 0,
deaths INTEGER DEFAULT 0,
assists INTEGER DEFAULT 0,
site TEXT NOT NULL,
side TEXT NOT NULL,
result_type TEXT NOT NULL,
FOREIGN KEY (round_id) REFERENCES Round (round_id)
)
''')

conn.commit()

"""
Adding matches and other data to tables
new_match adds a new match to the Match table
new_round adds a new match to the Round table, connected to its match based on the match_id;'key
new_user_stats is an extension in a seperate table for each round the holds the round_id key to link the data, and holds the stats for each round
"""

def new_match(date, map, result):
   cursor.execute('''
   INSERT INTO Match (date, map, result)
   VALUES (?, ?, ?)
   ''', (date, map, result))
   conn.commit()
   return cursor.lastrowid #returns new match_id

def new_round(match_id, round_number, result):
   round_id = f"{match_id}_{round_number}"
   
   cursor.execute('''
   INSERT INTO Round (round_id, match_id, round_number, result)
   VALUES (?, ?, ?, ?)
   ''', (round_id, match_id, round_number, result))
   conn.commit()
   return round_id #returns new round_id

def new_user_stats(round_id, operator, kills, deaths, assists, site, side, result_type):
   cursor.execute('''
   INSERT INTO UserStats (round_id, operator, kills, deaths, assists, site, side, result_type)
   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
   ''', (round_id, operator, kills, deaths, assists, site, side, result_type))
   conn.commit()

def change_result(match_id, res):
   cursor.execute('''
   UPDATE Match
   SET result = ?
   WHERE match_id = ?
   ''', (res, match_id))
   conn.commit()

"""
Querying data for use in visualization and data analysis
get_match_stats returns match stats based on match_id
"""
def match_table():
   cursor.execute("SELECT * FROM Match")
   rows = cursor.fetchall()
   return rows

def round_table():
   cursor.execute("SELECT * FROM Round")
   rows = cursor.fetchall()
   return rows

def user_stats_table(): 
   cursor.execute("SELECT * FROM UserStats")
   rows = cursor.fetchall()
   return rows

def get_match_stats(match_id):
   cursor.execute('''
   SELECT Round.round_number, UserStats.operator, UserStats.kills, UserStats.deaths, UserStats.assists, UserStats.site, UserStats.side, UserStats.result_type
   FROM Round
   JOIN UserStats ON Round.round_id = UserStats.round_id
   WHERE Round.match_id = ?
   ORDER BY Round.round_number
   ''', (match_id,))
   return cursor.fetchall()

def check_match(match_id):
   cursor.execute("SELECT * FROM Match WHERE match_id = ?", (match_id,))
   match = cursor.fetchone()
   print("Match Found:", match)

#testing

def reset_tables():
   cursor.execute("DROP TABLE IF EXISTS Match")
   cursor.execute("DROP TABLE IF EXISTS Round")
   cursor.execute("DROP TABLE IF EXISTS UserStats")
   conn.commit()
   conn.close()

