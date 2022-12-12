import numpy as np
import random
import re
from time import sleep

from variables import *


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
            level = input("Would you like to play in 'hard' mode?\nThis gives computer 3x chance to hit your boats.\nEnter 'hard' or press 'enter' for normal.\n").lower()
            if level == "hard":
                print("Playing in 'hard' mode.\n\n")
            else:
                print("Playing in 'normal' mode.\n\n")
            break
        elif human_game == "no":
            player_name = "Another Computer"
            all_positions_another_computer = all_positions_computer.copy()
            break
    return player_name, human_game, all_positions_computer, all_positions_another_computer, level


def random_positions_boat(size):
    """
    Generate a randomly positioned boat of given size and check it doesn't overflow board
    
    Args
        size (int): takes in the boat size
        
    Return
        boat_positions (list): list of tuple coordinates for the boat within the board
    """
    while True:
        x = board_dimensions[0] - 1
        y = board_dimensions[1] - 1
        boat_start = (random.randint(0, x), random.randint(0, y))
        north, south, east, west = ((1, 0), (-1, 0), (0, 1), (0, -1))
        direction = random.choice([north, south, east, west])
        
        x_positions = np.array([boat_start[0]+(i*direction[0]) for i in range(size)])
        if np.min(x_positions) < 0 or np.max(x_positions) > x:
            continue
        y_positions = np.array([boat_start[1]+(i*direction[1]) for i in range(size)])
        if np.min(y_positions) < 0 or np.max(y_positions) > y:
            continue
        return [(x, y) for x, y in zip(x_positions, y_positions)]
   
    
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
        x, y = ((int(c) - 1) for c in re.split('[ ,.-]', user_input))
        if check_coordinate_limits(x, y):
            return exit_game, x, y
    except ValueError:
        print("\nWARNING Gunners do not understand those coordinates, please try again\n")
        
             
def check_coordinate_limits(x, y):
    """
    Helper function to check input coordinates are on board
    """
    if (x < 0) or (x > board_dimensions[0] - 1) or (y < 0) or (y > board_dimensions[1] - 1):
        print(f"Please enter values between 1-{board_dimensions[0]} and 1-{board_dimensions[1]}")
        return False
    else:
        return True
    
            
def computer_select_coordinates(all_positions_player):
    """
    Selects a random coordinate for firing
    """
    random_coor = random.choice(all_positions_player)
    i = all_positions_player.index(random_coor)
    xx, yy = all_positions_player.pop(i)
    return xx, yy


def hard_turn(player_two, player_one, all_positions_computer, unfair_shots):
    """
    Gives unfair advantage with three attempts to hit boat for computer on each turn
    """
    while unfair_shots < 3:
        xx, yy = computer_select_coordinates(all_positions_computer)
        hit = player_two.fire(xx, yy, player_one)
        if hit == True:
            unfair_shots += 1
            return hit, unfair_shots
        else:
            unfair_shots += 1
    return hit, unfair_shots