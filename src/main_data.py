import database
from datetime import datetime

def add_match():
    """
    result must be "win" or "lose"
    game over when one team reaches 4 (win/loss = 4) and overtime starts when one team has 4 but the other has 3
    """
    match_id = database.new_match(date=datetime.now().strftime("%Y-%m-%d"), map=input("Map: "), result="NULL")
    win = 0
    lose = 0
    round_number = 0

    while win != 4 and lose != 4: #regulation
        round_number += 1
        result = input("Win or lose: ")
        if result == "win":
            win += 1
        elif result == "lose":
            lose += 1
        round_id = database.new_round(match_id, round_number, result)
        database.new_user_stats(round_id, operator=input("Operator: "), kills=input("Kills: "), deaths=input("Deaths: "), 
                                assists=input("Assists: "), site=input("Site: "), side=input("Attack or Defense: "), result_type=input("Time, Defuse, Team Eliminated: "))

    if win == 4 and lose <= 2: #round win regulation
        database.change_result(match_id, "win")
        print("match win")
        return
    
    elif lose == 4 and win <= 2: #round loss regulation
        database.change_result(match_id, "lose")
        print("match loss")
        return
    
    while win != 5 and lose != 5: #overtime
        round_number += 1
        result = input("Win or lose: ")
        if result == "win":
            win += 1
        elif result == "lose":
            lose += 1
        round_id = database.new_round(match_id, round_number, result)
        database.new_user_stats(round_id, operator=input("Operator: "), kills=input("Kills: "), deaths=input("Deaths: "), 
                                assists=input("Assists: "), site=input("Site: "), side=input("Attack or Defense: "), result_type=input("Time, Defuse, Team Eliminated: "))

    if win == 5: #round win overtime
        database.change_result(match_id, "win")
        print("match win")
        return
    
    elif lose == 5: #round loss overtime
        database.change_result(match_id, "lose")
        print("match loss")
        return

def sort_best_match(option):
    """
    Sort best match based on "Option"
    "Option" can be KDA or Kills
    Returns list of matches sorted in decreasing order based on option
    """
    user_stats = database.user_stats_table()
    data = []
    for round in user_stats:
        data.append({
            "round_id": round[1], 
            "kills": round[3],
            "deaths": round[4],
            "assists": round[5]
            })
    
    if option == "Kills":
        sorted_data = sorted(data, key=lambda x: x["kills"], reverse=True)
        print(sorted_data)
    elif option == "KD":
        pass
