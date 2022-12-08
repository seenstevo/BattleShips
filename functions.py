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
    #while True:
    opponent.board, hit, opponent.lives = current_player.fire(shot[0], shot[1], opponent.board, opponent.lives)
    return hit
        # if hit == False:
        #     break
        #if current_player.id != "Computer":
        #    print(f"Here is your shot history to plan your next move: {current_player.shots_board}")
        # if opponent.lives == 0:
        #     break