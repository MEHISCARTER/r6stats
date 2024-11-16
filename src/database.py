import sqlite3

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
conn = sqlite3.connect('STATS.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Match (
               match_id INTEGER PRIMARY KEY,
               date TEXT NOT NULL,
               map TEXT NOT NULL,
               result TEXT NOT NULL,
               )''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Round (
               round_id INTEGER PRIMARY KEY AUTOINCREMENT,
               match_id INTEGER NOT NULL,
               round_number INTEGER NOT NULL,
               result TEXT NOT NULL,
               FOREIGN KEY (match_id) REFERENCE Match (match_id)
               );
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS UserStats (
               stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
               round_id INTEGER NOT NULL,
               operator TEXT NOT NULL,
               kills INTEGER DEFAULT 0,
               deaths INTEGER DEFAULT 0,
               assists INTEGER DEFAULT 0,
               site TEXT NOT NULL,
               side TEXT NOT NULL,
               result_type TEXT NOT NULL,
               FOREIGN KEY (round_id) REERENCES Round (round_id)
               );
            ''')

conn.commit

def insert_match(date, map_name, outcome):