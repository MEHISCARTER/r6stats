import database
from datetime import datetime


def add_match(map_name, result, rounds):
    """
    Adds a match to the database with detailed round information.

    Args:
        map_name (str): The map name.
        result (str): The final match result ("win" or "lose").
        rounds (list of dict): Each dict contains round details, e.g.,
            {
                "result": "win",
                "side": "attack",
                "site": "staff room / open area",
                "kills": 6,
                "deaths": 4,
                "assists": 2,
                "operator": "ash",
                "result_type": "2:00, yes, yes"
            }

    Returns:
        int: The match ID.
    """

    try:
        # Prepare match data to save in the database
        match_data = []

        win = 0
        lose = 0

        for round_data in rounds:
            match_data.append({
                "side": round_data["side"],
                "site": round_data["site"],
                "kills": round_data["kills"],
                "deaths": round_data["deaths"],
                "assists": round_data["assists"],
                "operator": round_data["operator"],
                "result": round_data["result"]
            })

            # Track wins/losses
            if round_data["result"] == "win":
                win += 1
            elif round_data["result"] == "lose":
                lose += 1

        # Determine final result
        final_result = "win" if win > lose else "lose"

        # Save the match to the database
        match_id = database.save_match(match_data)
        database.change_result(match_id, final_result)
        return match_id

    except Exception as e:
        print(f"Error adding match: {e}")
        raise


def sort_best_match(option):
    """
    Sort the best match based on the specified option.

    Args:
        option (str): Criteria for sorting. Can be "Kills" or "KDA".

    Returns:
        list of dict: Matches sorted in decreasing order based on the option.
    """
    try:
        user_stats = database.get_user_stats()  # Ensure this function exists in your database module.
        data = []

        for round_stat in user_stats:
            data.append({
                "round_id": round_stat[1],
                "kills": round_stat[3],
                "deaths": round_stat[4],
                "assists": round_stat[5]
            })

        if option == "Kills":
            sorted_data = sorted(data, key=lambda x: x["kills"], reverse=True)
        elif option == "KDA":
            sorted_data = sorted(
                data,
                key=lambda x: (x["kills"] + x["assists"]) / max(1, x["deaths"]),
                reverse=True
            )
        else:
            raise ValueError("Invalid option. Must be 'Kills' or 'KDA'.")

        return sorted_data

    except Exception as e:
        print(f"Error sorting matches: {e}")
        raise
