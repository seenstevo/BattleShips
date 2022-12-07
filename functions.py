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
        boat_positions = [(x, y) for x, y in zip(x_positions, y_positions)]
        break
        
    return boat_positions

def check_boat(boat_positions, board):
    """
    Function to check whether boat can be added to board without breaking placing rules

    """
    # check no overlap with boat
    print(board[boat_positions])

boat_positions = random_positions_boat(1)
board = np.full((10, 10), "~")
print(boat_positions)
print(board)
print(board[boat_positions])
#check_boat(boat_positions, board)
###### get the value from board at positions of boat



