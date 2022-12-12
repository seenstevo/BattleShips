variables.py

boats: dictionary with all boats to be placed on board
board_dimension: tuple of board size
lives: int of total number of lives based on total boat spaces
water_sym: string character to represent water
boat_sym: string character to represent boat
hit_water_sym: string character to represent water hit by shot
hit_boat_sym: string character to represent hit boat position

class_Boat.py

class Boat:
    class attributes:
        boats: dictionary taken from variables
        board_dimension: tuple taken from variables
    class instance attributes:
        self.id: id name for player
        self.board: array representing players board
        self.shots_board: array representing shots by player
        self.lives: lives remaining for player
    methods:
        place_boats(): method to take possible positions for boat from random_positions_boat() method and place boats if positions possible, updating board.
        fire(): method to take shot coordinates by player and update the opponents board


functions.py

random_positions_boat(): get random boat positions for given boat
welcome_and_setup(): set up type of game and print basic game informatoin if human player
final_instructions(): show board to human player and give final instructions for firing



