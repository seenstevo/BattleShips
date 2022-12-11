import numpy as np
import random
import re

from variables import *


def random_positions_boat(size):
    """
    Generate a randomly positioned boat of given size and check it doesn't overflow board
    
    Args
        size (int): takes in the boat size
        
    Return
        boat_positions (list): list of tuple coordinates for the boat within the board
    """
    while True:
        # set random starting coordinate
        boat_start = (random.randint(0, 9), random.randint(0, 9))
        # create the 4 directions
        north, south, east, west = ((1, 0), (-1, 0), (0, 1), (0, -1))
        # select one of the 4 directions to extend the boat
        direction = random.choice([north, south, east, west])
        
        # generate the vectors in each orientation for boat positions
        x_positions = np.array([boat_start[0]+(i*direction[0]) for i in range(size)])
        y_positions = np.array([boat_start[1]+(i*direction[1]) for i in range(size)])
        # check we haven't overflown board, if so restart loop
        all_positions = np.concatenate((x_positions, y_positions))
        if np.min(all_positions) < 0 or np.max(all_positions) > (board_dimensions[0] - 1):
            continue
        # add coordinates of 
        return [(x, y) for x, y in zip(x_positions, y_positions)]
   
def welcome_and_setup():
    """
    Function to set up game type (human vs computer or computer vs computer) and take player name if required.
    Computer vs computer can be used for simulation or testing.
    """
    
    print("\n\nWelcome to battleships.\n\nYou will take turns attempting to fire on and sink ships placed on your opponents board.\nThe game will end once one player has lost all boats.\n")
    all_positions_computer = [(x, y) for x in range(board_dimensions[0]) for y in range(board_dimensions[1])]
    level = ""
    while True:
        human_game = input("\n'Yes' or 'No', you would like to play yourself? ('No' sets up a computer vs computer for simulation or testing.)\nYes or No?\n").lower()
        if human_game == "yes":
            player_name = input("\nWhat is your human name player?\n")
            print(f"\nWelcome {player_name}, good luck against the machine!\n")
            all_positions_another_computer = []
            level = input("Would you like to play in 'hard' mode?\nThis gives computer 3x chance to hit your boats.\nEnter 'hard' or press 'enter' for normal.\n")
            break
        elif human_game == "no":
            player_name = "Another Computer"
            all_positions_another_computer = all_positions_computer.copy()
            break
    return player_name, human_game, all_positions_computer, all_positions_another_computer, level



def final_instructions(lives, boats, player):
    """
    Simply print the starting board and final instructions for player.
    
    Args
        lives (int): how many lives each player has to start
        boats (dict): all boats to be placed for each board
        player (class Board instance): this gets the player instance from which we get the id and board with boats placed
    """
    print(f"{player.id}, here are your boats:\n\n{player.board}")
    print("\nInstructions:\n\n\t- To fire, enter coordinates (two values 1-10 separated by a comma or space. E.g. 2,6 or 2 6)")
    print(f"\t- If you are successful, you can fire again.")
    print(f"\t- You have a total of {lives} lives between your {len(boats)} boats.")
    print("\t- To exit game, when asked to insert coordinates, enter 'EXIT'\n")
    print("Let battle commence!!!!\n")
    
    
def human_turn(user_input):
    """
    For human player turn, checks user input for legal coordinates
    
    Args:
        user_input (str): user typed input
        
    Returns:
        exit_game (bool): should game be exited?
        x (int): coordinate in x-axis (rows). or "x" string if game to be exited
        y (int): coordinate in y-axis (columns). or "y" string if game to be exited
        
    Raises:
        ValueError if no valid coordinates have been entered
    """
    exit_game = False
    x, y = "x", "y"    
    if user_input == "exit":
        exit_game = True
        return exit_game, x, y
    try:
        x, y = ((int(c) -1) for c in re.split('[ ,.-]', user_input))
        if check_coordinate_limits(x, y):
            return exit_game, x, y
    except ValueError:
        print("\nWARNING Gunners do not understand those coordinates, please try again\n")
        
             
def check_coordinate_limits(x, y):
    """
    Helper function to check input coordinates are on board
    """
    if (x < 1) or (x > board_dimensions[0]) or (y < 1) or (y > board_dimensions[1]):
        print(f"Please enter values between 1-{board_dimensions[0]} and 1-{board_dimensions[1]}")
        return False
    else:
        return True
    
            
def computer_turn(all_positions_player):
    """
    Selects a random coordinate for firing
    """
    random_coor = random.choice(all_positions_player)
    i = all_positions_player.index(random_coor)
    xx, yy = all_positions_player.pop(i)
    return xx, yy


def reporting(human_game, player_one, player_two):
    """
    simple report of shots fired and success rate
    """
    if human_game == "yes":
        try:
            hits = np.count_nonzero(player_one.shots_board == hit_boat_sym)
            misses = np.count_nonzero(player_one.shots_board == hit_water_sym)
            success_rate = hits / (hits + misses) * 100
            print(f"- Total fired shots by {player_one.id}: {hits + misses} with a success rate of {success_rate:.2f}")
            hits = np.count_nonzero(player_two.shots_board == hit_boat_sym)
            misses = np.count_nonzero(player_two.shots_board == hit_water_sym)
            success_rate = hits / (hits + misses) * 100
            print(f"- Total fired shots by {player_two.id}: {hits + misses} with a success rate of {success_rate:.2f}\n")
        except:
            pass
    
def preround(human_game, player_one, player_two, round_no):
    """
    
    """
    print("#"*20 + f" Round {round_no} " + "#"*20 + "\n")
    if human_game == "yes":
        print(f"{player_one.id} Your board and your boats look like this:\n")
        print(player_one.board)
        print(f"\nLives remaining: {player_one.id} has {player_one.lives}, and {player_two.id} has {player_two.lives}")
        if human_game == "yes":
            input("\nHit 'Enter' to continue with your turn\n")
            

def hard_turn(player_two, player_one, all_positions_computer):
    """
    Gives unfair advantage with three attempts to hit boat for computer on each turn
    """
    unfair_shots = 3
    while unfair_shots > 0:
        xx, yy = computer_turn(all_positions_computer)
        hit = player_two.fire(xx, yy, player_one)
        if hit == True:
            unfair_shots = 0
        unfair_shots -= 1
    return hit