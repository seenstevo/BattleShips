import numpy as np

from variables import *


def final_instructions():
    """
    Simply print the starting board and final instructions for player.
    
    Args
        lives (int): how many lives each player has to start
        boats (dict): all boats to be placed for each board
        player (class Board instance): this gets the player instance from which we get the id and board with boats placed
    """
    print("\nInstructions:\n\n\t- To fire, enter coordinates (two values 1-10 separated by a ',', '.', '-' or a space. E.g. 2,6 or 2 6)")
    print(f"\t- If you are successful, you can fire again.")
    print(f"\t- You have a total of {lives} lives between your {len(boats)} boats.")
    print("\t- To exit game, when asked to insert coordinates, enter 'EXIT'\n")
    input("Press 'enter' when you are ready to begin.\n")
    print("Let battle commence!!!!\n")
        
    
def preround_reporting(human_game, player_one, player_two, round_no):
    """
    Print to screen the board, lives left and stats on success rates of each player
    """
    print("#"*20 + f" Round {round_no} " + "#"*20 + "\n")
    if human_game == "yes":
        print(f"{player_one.id}, your board and your boats look like this:\n")
        print(f"{player_one.board}\n")
        try:
            hits = np.count_nonzero(player_one.shots_board == hit_boat_sym)
            misses = np.count_nonzero(player_one.shots_board == hit_water_sym)
            success_rate = hits / (hits + misses) * 100
            print(f"- Total shots fired by {player_one.id}:\t\t{hits + misses} with a success rate of {success_rate:.2f}")
            hits = np.count_nonzero(player_two.shots_board == hit_boat_sym)
            misses = np.count_nonzero(player_two.shots_board == hit_water_sym)
            success_rate = hits / (hits + misses) * 100
            print(f"- Total shots fired by {player_two.id}:\t{hits + misses} with a success rate of {success_rate:.2f}")
        except:
            pass
        print(f"- Lives remaining:\t\t\t{player_one.id} has {player_one.lives}, and {player_two.id} has {player_two.lives}")
        if human_game == "yes":
            input("\nHit 'Enter' to continue with your turn\n")
            

def welcome_logo():
    print("\n     ,     ,     ,\n    / \\   / \\   / \\\n   /___\\ /___\\ /___\\\n   |/ \\| |/ \\| |/ \\|\n   /   \\ /   \\ /   \\\n  /     \\/     \\/     \\\n /       /       /       \\\n/_________/_________/_________\\")