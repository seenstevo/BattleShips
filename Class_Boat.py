from variables import *
from battleship_game_functions import *
import numpy as np

class Board:
    """
    
    """
    boats = boats
    board_dimensions = board_dimensions
    lives = lives
    board = np.full(board_dimensions, "~")
    
    def __init__(self, id):
        self.id = id
    
    def place_boats(self):
        for boat in boats:
            size = boats[boat]
            while True:
                boat_positions = random_positions_boat(size)
                
            
            return boat_positions
    
    def check_boat_positions(self):
        pass
    
    
        
    
    
player_board = Board
print(dir(player_board))



        
        
        
    