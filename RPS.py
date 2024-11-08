# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return "R" 

    move_counts = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S"),
    }
    
    if move_counts["R"] > move_counts["P"] and move_counts["R"] > move_counts["S"]:
        return "P"  
    elif move_counts["P"] > move_counts["S"]:
        return "S" 
    else:
        return "R"  
