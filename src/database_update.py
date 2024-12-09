import sqlite3

def save_match_with_map(map_name, match_data):
    connection = sqlite3.connect("r6_stats.db")
    cursor = connection.cursor()

    # Ensure a table for matches exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS match_stats (
            match_id INTEGER,
            round_number INTEGER,
            side TEXT,
            site TEXT,
            kills INTEGER,
            deaths INTEGER,
            assists INTEGER,
            operator TEXT,
            result TEXT,
            map_name TEXT
        )
    ''')

    # Get the next match ID
    cursor.execute("SELECT IFNULL(MAX(match_id), 0) + 1 FROM match_stats")
    match_id = cursor.fetchone()[0]

    # Save each round with its respective round number and map name
    for round_number, round_data in enumerate(match_data, start=1):
        cursor.execute('''
            INSERT INTO match_stats (
                match_id, round_number, side, site, kills, deaths, assists, operator, result, map_name
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            match_id,
            round_number,
            round_data["side"],
            round_data["site"],
            round_data["kills"],
            round_data["deaths"],
            round_data["assists"],
            round_data["operator"],
            round_data["result"],
            map_name
        ))

    connection.commit()
    connection.close()

    return match_id


def get_match_stats(match_id):
    connection = sqlite3.connect("r6_stats.db")
    cursor = connection.cursor()

    # Retrieve match stats and map name for the given match ID
    cursor.execute('''
        SELECT match_id, side, site, kills, deaths, assists, operator, result, map_name
        FROM match_stats
        WHERE match_id = ?
        ORDER BY round_number
    ''', (match_id,))

    match_stats = cursor.fetchall()
    connection.close()

    return match_stats
