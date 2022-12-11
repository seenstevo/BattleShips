from time import sleep
import random

from functions import *
from class_Boat import *
from variables import *

def main():
    
    player_name, human_game, all_positions_computer, all_positions_another_computer, level = welcome_and_setup()
    
    player_one = Board(player_name)
    player_two = Board("Computer")

    # Now place the boats for both boards using the place_boats method
    player_one.place_boats() 
    player_two.place_boats()
    
    sleep_time = 0
    if human_game == "yes":
        final_instructions(lives, boats, player_one)
        del all_positions_another_computer
        sleep_time = 2
    
    
#### Game is ready to commence! Initialise Round 1 ###################

    round_no = 1
    exit_game = False

    while True:
        
        preround(human_game, player_one, player_two, round_no)
        reporting(human_game, player_one, player_two)

 ####### Player Turn #################################################
        while True:
            if human_game == "yes":
                print("\nBefore you shoot, here is your shots history:")
                try:
                    print(f"Reminder: Your last shot was at {x+1}-{y+1}\n")
                except:
                    pass
                print(f"\n{player_one.shots_board}")
                user_input = input("\nEnter coordinates:\n").lower()
                try:
                    exit_game, x, y = human_turn(user_input)
                except:
                    continue
                
            if exit_game == True:
                break
                          
            elif human_game == "no":
                x, y = computer_turn(all_positions_another_computer)

            hit = player_one.fire(x, y, player_two)
            
            if hit == False:
                break
            
        if exit_game == True:
            print("\nLeaving game\n")
            break

        if player_two.lives == 0:
            print(f"\nCongratulations {player_one.id}, you have beaten the computer with {player_one.lives} lives remaining!\n")
            break
        
        if human_game == "yes":
            input("\nHit 'Enter' to continue with opponents turn")
        
 ####### Computer Turn ###############################################  
      
        while True:

            if human_game == "yes":
                print("\nComputer taking aim!")
                sleep(sleep_time)
            
            if level == "hard":
                hit = hard_turn(player_two, player_one, all_positions_computer)
            else:
                xx, yy = computer_turn(all_positions_computer)
                hit = player_two.fire(xx, yy, player_one)
            
            if hit == False:
                break

        if player_one.lives == 0:
            print(f"Unlucky {player_one.id}, you have been beaten the computer who had {player_two.lives} lives remaining!")
            break
      
        round_no += 1

    # Game is finished so print summary of final boards
    if exit_game == False: 
        print(f"\nAfter {round_no} rounds, the final boards looked like this:\n\n {player_one.id}'s board:\n\n {player_one.board} \n\nComputer board:\n\n {player_two.board}\n")
        
    
if __name__ == "__main__":
    main()
    