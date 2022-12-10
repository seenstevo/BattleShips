import numpy as np
import random

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
    

def turn(current_player, opponent, shot):
    """
    Takes the coordinates of a shot and updates opponent board and lives. Allows further shots while current shot is successful.
    Uses Board.fire() method
    
    Args
        current_player (class Board instance): the Board.fire() method called for player taking current turn
        opponent (class Baord instance): latest version of opponents board
        shot (tuple): x and y coordinates of the shot
        
    Returns
        None
    """
    opponent.board, hit, opponent.lives = current_player.fire(shot[0], shot[1], opponent.board, opponent.lives)
    return hit

def welcome_and_setup():
    """
    Function to set up game type (human vs computer or computer vs computer) and take player name if required.
    Computer vs computer can be used for simulation or testing.
    """
    
    print("\n\nWelcome to battleships.\n\nYou will take turns attempting to fire on and sink ships placed on your opponents board.\nThe game will end once one player has lost all boats.\n")
    all_positions_computer = [(x, y) for x in range(board_dimensions[0]) for y in range(board_dimensions[1])]
    
    while True:
        human_game = input("\n'Yes' or 'No', you would like to play yourself? ('No' sets up a computer vs computer for simulation or testing.)\nYes or No?\n").lower()
        if human_game == "yes":
            player_name = input("\nWhat is your human name player?\n")
            print(f"\nWelcome {player_name}, good luck against the machine!\n")
            all_positions_another_computer = []
            break
        elif human_game == "no":
            player_name = "Another Computer"
            all_positions_another_computer = [(x, y) for x in range(board_dimensions[0]) for y in range(board_dimensions[1])]
            break
    return player_name, human_game, all_positions_computer, all_positions_another_computer



def final_instructions(lives, boats, player):
    """
    Simply print the starting board and final instructions for player.
    
    Args
        lives (int): how many lives each player has to start
        boats (dict): all boats to be placed for each board
        player (class Board instance): this gets the player instance from which we get the id and board with boats placed
    """
    print(f"{player.id}, here are your boats:\n\n{player.board}")
    print("\nInstructions:\nTo fire, enter coordinates (two values 1-10 separated by a comma or space. E.g. 2,6 or 2 6)\n")
    print(f"If you are successful, you can fire again.\nYou have a total of {lives} lives between your {len(boats)} boats.\n")
    print("To exit game, when asked to insert coordinates, enter 'EXIT'\n")
    print("Let battle commence!!!!\n")
    
    
def human_turn(user_input, player):
    """
    
    """
    exit_game = False
    x, y = 0, 0    
    if user_input == "exit":
        exit_game = True
        return exit_game, x, y
    try:
        x, y = (int(c) - 1 for c in user_input.split(","))
        return exit_game, x, y
    except ValueError:
        try:
            x, y = (int(c) - 1 for c in user_input.split())
            return exit_game, x, y
        except ValueError:
            print("\nWARNING Gunners do not understand those coordinates, please try again\n")
            
            
            
def computer_turn(all_positions_player):
    """
    
    """
    random_coor = random.choice(all_positions_player)
    i = all_positions_player.index(random_coor)
    xx, yy = all_positions_player.pop(i)
    return xx, yy


def reporting(player_turn, opponent):
    """
    
    """
    hits = np.count_nonzero(player_turn.shots_board == hit_boat_sym)
    misses = np.count_nonzero(player_turn.shots_board == hit_water_sym)
    success_rate = hits / (hits + misses) * 100
    print(f"Total fired shots by {player_turn.id}: {hits + misses} with a success rate of {success_rate:.2f}\n")
    
