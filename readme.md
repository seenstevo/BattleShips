# Battleships game implemented in python
## by Sean Stevenson

## About The Game

This game involves two players who each place a set number of boats on a board. The players then take it in turns "firing" on the opponents boats without seeing their locations attempting to sink them. Each boat requires a hit at each location of the boat to be "sunk". The game ends when one player has lost all their boats.

## Special implementation in this game

- This standard implementation involves a human player playing against the computer. The player has the option to select a "hard" mode whereby the computer, while choosing all shots randomly, has 3 attempts on each turn.
- Default settings are: a 10x10 board with 10 boats in total making up 20 "lives". These settings (including the graphics of the board) can be changed in the variables.py file.
- A second game option is computer vs computer mode whereby simulations or testing can be run with the game completing in a few seconds.

## The file system

- main.py:            principal script for running the game which controls logic flow.
- Boat.py:            definition of the attributes and methods for the Board class. each game involves two instances of this class, one for each player.
- functions.py:       contains helper functions outside scope of the class Board.
- functions_print.py  contains all functions relating to prints including game set up
- readme.md:          this readme
- variables.py        constants used to configure game


## Overview of Key Objects in each file


### **variables.py**

boats:              dictionary with all boats to be placed on board (default 10 boats: 4x1, 3x2, 2x3 and 1x4)  
board_dimension:    tuple of board size (default (10,10))  
lives:              int of total number of lives based on total boat spaces (default 20)  
water_sym:          string character to represent water (default " ")  
boat_sym:           string character to represent boat (default "O")  
hit_water_sym:      string character to represent water hit by shot (default "*")  
hit_boat_sym:       string character to represent hit boat position (default "X")


### **Boat.py**

**instance attributes**

-self.id: id name for player  
-self.board: array representing players board  
-self.shots_board: array representing shots by player  
-self.lives: lives remaining for player  
**methods**

-place_boats(): method to take possible positions for boat from random_positions_boat() method and place boats if positions possible, updating board.  
-fire(): method to take shot coordinates by player and update the opponents board  


### **functions.py**

**random_positions_boat()**
-get random boat positions for given boat

**welcome_and_setup()**
-set up type of game and print basic game informatoin if human player

**human_turn()**
-controls input from human player

**check_coordinate_limits()**
-checks user input is on board

**computer_select_coordinates()**
-chose computer coordinates from list of coordinates

**hard_turn()**
-logic flow for hard mode allowing 3 shots per turn for computer


### **functions_print.py**

**final_instructions()**
-show board to human player and give final instructions for firing

**preround_reporting()**
-print summary of game and stats after each round