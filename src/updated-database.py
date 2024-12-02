import sqlite3

def save_match(match_data):
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
            result TEXT
        )
    ''')

    # Get the next match ID
    cursor.execute("SELECT IFNULL(MAX(match_id), 0) + 1 FROM match_stats")
    match_id = cursor.fetchone()[0]

    # Save each round with its respective round number
    for round_number, round_data in enumerate(match_data, start=1):
        cursor.execute('''
            INSERT INTO match_stats (
                match_id, round_number, side, site, kills, deaths, assists, operator, result
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            match_id,
            round_number,
            round_data["side"],
            round_data["site"],
            round_data["kills"],
            round_data["deaths"],
            round_data["assists"],
            round_data["operator"],
            round_data["result"]
        ))

    connection.commit()
    connection.close()

    return match_id

def get_match_stats(match_id):
    connection = sqlite3.connect("r6_stats.db")
    cursor = connection.cursor()

    # Retrieve all rounds for the given match ID
    cursor.execute('''
        SELECT round_number, side, site, kills, deaths, assists, operator, result
        FROM match_stats
        WHERE match_id = ?
        ORDER BY round_number
    ''', (match_id,))
    match_stats = cursor.fetchall()

    connection.close()
    return match_stats
