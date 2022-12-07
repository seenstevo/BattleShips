import battleship_game_functions as bgf
from classes import *

def main():
    
    player_name = input("What is your name player?\n")
    
    player = Board(player_name)
    computer = Board("Computer")
    
    player_position = player.place_boats()
    
    
    print(player_position)
    print(player.id)
    
    
    
    
if __name__ == "__main__":
    main()
    