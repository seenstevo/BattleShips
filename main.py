from time import sleep
import random

from functions import turn, welcome_setup, final_instructions
from Class_Boat import *
from variables import *

def main():
    
    player_name, human_game = welcome_setup()
    
    player = Board(player_name)
    computer = Board("Computer")

    # Now place the boats for both boards using the place_boats method
    player.place_boats() 
    computer.place_boats()
    print("\nBoats placed\n")
    
    if human_game == "yes":
        final_instructions(board_dimensions, lives, boats, player)
    
    
#### Game is ready to commence! Initialise Round 1 ###################

    round = 1
    # here we create the list of coordinates for the computer to randomly select from without replacement
    all_positions_computer = [(x, y) for x in range(10) for y in range(10)]
    # for demo only
    if human_game == "no":
        all_positions_player = [(x, y) for x in range(10) for y in range(10)]

    while True:
        
        print("#"*20 + f" Round {round} " + "#"*20 + "\n")
        exit_game = False

 ####### Player Turn #################################################    

        while True:
            print("Before you shoot, here is your shots history:\n")
            print(player.shots_board)       
            # Take player shot coordinates
            if human_game == "yes":
                user_input = input("\nEnter coordinates:\n")
                if user_input == "exit":
                    exit_game = True
                    break
                x, y = (int(c) - 1 for c in user_input.split(","))
            elif human_game == "no":
                random_coor = random.choice(all_positions_player)
                i = all_positions_player.index(random_coor)
                x, y = all_positions_player.pop(i)
            
            # take the turn
            hit = turn(player, computer, (x, y))
            if hit == False:
                break
        
        if exit_game == True:
            print("\nLeaving game\n")
            break
            
        # add reporting function to run after both turns
        hits = np.count_nonzero(player.shots_board == hit_boat_sym)
        misses = np.count_nonzero(player.shots_board == hit_water_sym)
        success_rate = hits / (hits + misses) * 100
        print(f"Total fired shots {hits + misses} with a success rate of {success_rate:.2f}%\nComputer has {computer.lives} lives left")
        
######## Check Computer Still Has Lives ##############################

        if computer.lives == 0:
            print(f"Congratulations player {player.id}, you have beaten the computer!")
            break
        
 ####### Computer Turn ###############################################  
      
        while True:
            print("Computer taking aim!")
            if human_game == "yes":
                sleep(2)
            # Take the shot coordinates
            random_coor = random.choice(all_positions_computer)
            i = all_positions_computer.index(random_coor)
            random_shot = all_positions_computer.pop(i)
            # Take turn of computer
            hit = turn(computer, player, random_shot)
            if hit == False:
                break
        
        if exit_game == True:
            print("\nLeaving game\n")
            break
            
        hits = np.count_nonzero(computer.shots_board == hit_boat_sym)
        misses = np.count_nonzero(computer.shots_board == hit_water_sym)
        success_rate = hits / (hits + misses) * 100
        print(f"Total shots on your water: {hits + misses}, with a success rate of {success_rate:.2f}%.\nYou have {player.lives} lives left")
            
######## Check Player Still Has Lives ################################

        if player.lives == 0:
            print(f"Unlucky player {player.id}, you have been beaten the computer!")
            break
        
        print("After the computer turn, your board looks like this now:\n")
        print(player.board)
        
######## Next Round ##################################################  
      
        round += 1
        
######## Game Over ################################################## 

    # Game is finished so print summary of final boards   
    print(f"Final boards looked like this, was it close?\n\ {player.id} board:\n\n {player.board} \n\nComputer board:\n\n {computer.board}")    
    
    
if __name__ == "__main__":
    main()
    