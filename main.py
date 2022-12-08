from time import sleep

from functions import *
from Class_Boat import *
from variables import *

def main():
    
    human_game = input("True or False, you would like to play yourself?\nSetting to False sets up a computer vs computer simulation.\n")
    if human_game == "True":
        player_name = input("What is your name player?\n")
    else:
        player_name = "Another_Computer"
    
    # set up boards with Board instances for player and computer
    player = Board(player_name)
    computer = Board("Computer")

    # Now place the boats for both boards using the place_boats method
    player.place_boats() 
    computer.place_boats()
    print("\nBoats placed\n")
    print(f"{player.id}, here are your boats:\n\n{player.board}")
    print("\nInstructions:\nTo fire, enter coordinates for x and y axis with values 1 to 10\nIf you are successful, you can fire again.\nYou have a total of 20 lives between your 10 boats.\n")
    print("To exit game, when asked to insert coordinates, enter 'EXIT'\n")
    print("Let battle commence!!!!\n")
    
#### Game is ready to commence! Initialise Round 1 ###################

    round = 1
    # here we create the list of coordinates for the computer to randomly select from without replacement
    all_positions_computer = [(x, y) for x in range(10) for y in range(10)]
    # for demo only
    if human_game == "False":
        all_positions_player = [(x, y) for x in range(10) for y in range(10)]

    while True:
        print("#"*20 + f" Round {round} " + "#"*20 + "\n")

 ####### Player Turn #################################################    

        while True:
            print("Before you shoot, here is your shots history:\n")
            print(player.shots_board)       
            # Take player shot coordinates
            if human_game == "True":
                x, y = ((int(c) - 1) for c in input("\nEnter coordinates:\n").split())
            else:
                random_coor = random.choice(all_positions_player)
                i = all_positions_player.index(random_coor)
                x, y = all_positions_player.pop(i)
            
            # take the turn
            hit = turn(player, computer, (x, y))
            if hit == False:
                break
            
        hits = np.count_nonzero(player.shots_board == hit_boat_sym)
        misses = np.count_nonzero(player.shots_board == hit_water_sym)
        print(f"Total fired shots {hits + misses} with a success rate of {hits / (hits + misses) * 100}\nComputer has {computer.lives} lives left")
        
######## Check Computer Still Has Lives ##############################

        if computer.lives == 0:
            print(f"Congratulations player {player.id}, you have beaten the computer!")
            break
        
 ####### Computer Turn ###############################################  
      
        while True:
            print("Computer taking aim!")
            if human_game == "False":
                sleep(2)
            # Take the shot coordinates
            random_coor = random.choice(all_positions_computer)
            i = all_positions_computer.index(random_coor)
            random_shot = all_positions_computer.pop(i)
            # Take turn of computer
            hit = turn(computer, player, random_shot)
            if hit == False:
                break
            
        hits = np.count_nonzero(computer.shots_board == hit_boat_sym)
        misses = np.count_nonzero(computer.shots_board == hit_water_sym)
        print(f"Total shots on your water: {hits + misses}, with a success rate of {hits / (hits + misses) * 100}.\nYou have {player.lives} lives left")
            
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
    print(f"Final boards looked like this, was it close?\n\nPlayer {player.id} board:\n\n {player.board} \n\nComputer board:\n\n {computer.board}")       
        
        
        
        
        
        # while True:
        #     random_coor = random.choice(all_positions_player)
        #     i = all_positions_player.index(random_coor)
        #     shot_location = all_positions_player.pop(i)
        #     #shot_location = [int(c) for c in input("\nEnter coordinates, row then column. E.g 2 5:\n").split()]
        #     # add check for values
        #     computer.board, hit, computer.lives = player.fire(shot_location[0],shot_location[1], computer.board, computer.lives)
        #     if hit == False:
        #         break
        #     print(f"Here is your shot history to plan your next move: {player.shots_board}")
        #     if computer.lives == 0:
        #         break      
        
        

    
    
    
if __name__ == "__main__":
    main()
    