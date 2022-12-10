from time import sleep
import random

from functions import turn, welcome_and_setup, final_instructions, human_turn, computer_turn, reporting
from Class_Boat import *
from variables import *

def main():
    
    player_name, human_game, all_positions_computer, all_positions_another_computer = welcome_and_setup()
    
    player = Board(player_name)
    computer = Board("Computer")

    # Now place the boats for both boards using the place_boats method
    player.place_boats() 
    computer.place_boats()
    
    sleep_time = 0
    if human_game == "yes":
        final_instructions(lives, boats, player)
        del all_positions_another_computer
        sleep_time = 2
    
    
#### Game is ready to commence! Initialise Round 1 ###################

    round = 1

    while True:
        
        print("#"*20 + f" Round {round} " + "#"*20 + "\n")
        exit_game = False
        print("Your board and your boats look like this:\n")
        print(player.board)
        print(f"\nLives remaining: {player.id} has {player.lives}, and {computer.id} has {computer.lives}")
        sleep(sleep_time)
        if human_game == "yes":
            input("\nHit 'Enter' to continue with your turn")

 ####### Player Turn #################################################
        while True:
            if human_game == "yes":
                print("\nBefore you shoot, here is your shots history:")
                try:
                    print(f"Reminder: Your last shot was at {x+1}-{y+1}\n")
                except:
                    pass
                print(f"\n{player.shots_board}")
                user_input = input("\nEnter coordinates:\n").lower()
                exit_game, x, y = human_turn(user_input, player)
                
            if exit_game == True:
                break
                          
            elif human_game == "no":
                x, y = computer_turn(all_positions_another_computer)
                
            hit = turn(player, computer, (x, y))
            
            if hit == False:
                break
            
        if exit_game == True:
            print("\nLeaving game\n")
            break
        
        if human_game == "yes":
            input("\nHit 'Enter' to continue with opponents turn")
            reporting(player, computer)

        if computer.lives == 0:
            print(f"\nCongratulations {player.id}, you have beaten the computer with {player.lives} lives remaining!\n")
            break
        
 ####### Computer Turn ###############################################  
      
        while True:

            if human_game == "yes":
                print("Computer taking aim!")
                sleep(sleep_time)

            xx, yy = computer_turn(all_positions_computer)

            hit = turn(computer, player, (xx, yy))
            
            if hit == False:
                break
            
        reporting(computer, player)

        if player.lives == 0:
            print(f"Unlucky {player.id}, you have been beaten the computer who had {computer.lives} lives remaining!")
            break
      
        round += 1

    # Game is finished so print summary of final boards
    if exit_game == False: 
        print(f"\nFinal boards looked like this:\n\n {player.id}'s board:\n\n {player.board} \n\nComputer board:\n\n {computer.board}\n")
        
    
if __name__ == "__main__":
    main()
    