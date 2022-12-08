import numpy as np

from variables import *
from functions import *


class Board:
    """
    
    """
    boats = boats
    board_dimensions = board_dimensions
    
    def __init__(self, id):
        self.id = id
        self.board = np.full(self.board_dimensions, water_sym)
        self.shots_board = np.full(self.board_dimensions, water_sym)
        self.lives = lives
    
    def place_boats(self):
        """
        Loop through boat objects and place them on board such that none overlap.
        Update self.board with the 10 placed boats
        """
        for boat in boats:
            size = boats[boat]
            while True:
                boat_positions = random_positions_boat(size)
                state_positions = [self.board[position] for position in boat_positions]
                if boat_sym in state_positions:
                    continue
                else:
                    for position in boat_positions:
                        self.board[position] = boat_sym
                break

    def fire(self, x, y, opponent_board, opponent_lives):
        """
        Takes x and y positions for a shot and updates board 
        """
        what_hit = opponent_board[x, y]
        if what_hit == boat_sym:
            print("\nYou've hit a ship!\nFire again!\n")
            opponent_board[x, y] = hit_boat_sym
            self.shots_board[x,y] = hit_boat_sym
            hit = True
            opponent_lives = opponent_lives - 1
        elif what_hit == water_sym:
            print("\nSplash! That missed!\n")
            opponent_board[x, y] = hit_water_sym
            self.shots_board[x,y] = hit_water_sym
            hit = False
        else:
            print("\nYou already blew this place up!\n")
            hit = False
        return opponent_board, hit, opponent_lives
    
        
        
        
        
        
    
    
#player_board = Board("Sean")
#print(player_board.board)
#print(player_board.place_boats())
#print(player_board.board)



        
        
        
    