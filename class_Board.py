import numpy as np
from time import sleep

from variables import *
from functions import random_positions_boat


class Board:
    """
    Class for Board object. 
    Sets up 2 boards per player on which boats are placed and game progress is updated as well a shots fired board
    
    Args:
        id (str): player name
    """
    
    def __init__(self, id):
        """
        Class Board generator taking id (str) argument for player name.
        Generates two boards per player, one for updating status of players boats and the other for their shots
        Also generates the total lives value
        """
        self.id = id
        self.board = np.full(board_dimensions, water_sym)
        self.shots_board = np.full(board_dimensions, water_sym)
        self.lives = lives
    
    def place_boats(self):
        """
        Loop through boat objects and place them on board such that none overlap.
        Update self.board with the 10 placed boats
        Uses the random_positions_boat function to assign coordinates for checking
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

    def fire(self, x, y, opponent):
        """
        Takes x and y positions for a shot and updates both opponent board and self.shots_board
        """
        what_hit = opponent.board[x, y]
        if what_hit == boat_sym:
            opponent.board[x, y] = hit_boat_sym
            self.shots_board[x,y] = hit_boat_sym
            hit = True
            opponent.lives = opponent.lives - 1
            if opponent.lives == 0:
                print(f"{self.id} turn: Bingo, a ship has been hit! That was the last of the enemy!\n")
                print("          _ ._  _ , _ ._\n        (_ ' ( `  )_  .__)\n      ( (  (    )   `)  ) _)\n     (__ (_   (_ . _) _) ,__)\n         `~~`\\ ' . /`~~`\n              ;   ;\n              /   \\\n_____________/_ __ \\_____________\n")
                sleep(3)
            else:
                print(f"{self.id} turn: Bingo, a ship has been hit! Fire again!\n")
                print("          _ ._  _ , _ ._\n        (_ ' ( `  )_  .__)\n      ( (  (    )   `)  ) _)\n     (__ (_   (_ . _) _) ,__)\n         `~~`\\ ' . /`~~`\n              ;   ;\n              /   \\\n_____________/_ __ \\_____________\n")
        elif what_hit == water_sym:
            print(f"\n{self.id} turn: Splash! That missed!\n")
            opponent.board[x, y] = hit_water_sym
            self.shots_board[x,y] = hit_water_sym
            hit = False
        else:
            print(f"\n{self.id} turn: You already blew this place up!\n")
            hit = False
        return hit


        
        
        
    