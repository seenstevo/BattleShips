from time import sleep

from functions import *
from functions_print import *
from Board import *
from variables import *

def main():
    
    welcome_logo()
    
    player_name, human_game, all_positions_computer, all_positions_another_computer, level = welcome_and_setup()
    
    player_one = Board(player_name)
    player_two = Board("Computer")

    # Now place the boats for both boards using the place_boats method
    player_one.place_boats() 
    player_two.place_boats()
    
    if human_game == "yes":
        final_instructions()
        sleep(2)
        del all_positions_another_computer    

    round_no = 1
    exit_game = False
    
    # Start Round 1
    while True:
        
        preround_reporting(human_game, player_one, player_two, round_no)

        # player_one turn
        while True:
            
            if human_game == "yes":
                try:
                    print(f"\nBefore you shoot, here are your previous shots. (Your last shot was at {x+1}-{y+1}):\n")
                except:
                    print("\nBefore you shoot, here is your shots history:")
                print(f"\n{player_one.shots_board}")
                user_input = input("\nEnter coordinates:\n").lower()
                try:
                    exit_game, x, y = human_turn(user_input)
                    if exit_game == True:
                        break
                except:
                    continue
                          
            elif human_game == "no":
                x, y = computer_select_coordinates(all_positions_another_computer)

            hit = player_one.fire(x, y, player_two)
            
            if hit == False or (player_two.lives == 0):
                break
            
        if player_two.lives == 0:
            print(f"\nCongratulations {player_one.id}, you have beaten the computer with {player_one.lives} lives remaining!\n")
            break
            
        if exit_game == True:
            print("\nLeaving game\n")
            break
        
        if human_game == "yes":
            input("\nHit 'Enter' to continue with opponents turn")
         
        # player_two turn
        unfair_shots = 0
        while True:

            if human_game == "yes":
                print("\nComputer taking aim!\n")
                sleep(2)
            
            if level == "hard":
                hit, unfair_shots = hard_turn(player_two, player_one, all_positions_computer, unfair_shots)
            else:
                xx, yy = computer_select_coordinates(all_positions_computer)
                hit = player_two.fire(xx, yy, player_one)
            
            if hit == False or (player_one.lives == 0):
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
    