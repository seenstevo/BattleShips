from time import sleep
import functions as bgf
from Class_Boat import *

def main():
    
    player_name = input("What is your name player?\n")
    #player_name = "Sean"
    
    # set up boards with Board instances for player and computer
    player = Board(player_name)
    computer = Board("Computer")

    # Now place the boats for both boards using the place_boats method
    player.place_boats() 
    computer.place_boats()
    print("Boats placed, let battle commence!!!!\n")
    print(f"{player.id}, here are your boats:\n\n{player.board}")
    
    ###################################################################
    # Game is ready to commence!
    round = 1
    while True:
        print("#"*60)
        print(f"Round {round}\n")
        # Player turn
        all_positions_player = [(x, y) for x in range(10) for y in range(10)]
        while True:
            random_coor = random.choice(all_positions_player)
            i = all_positions_player.index(random_coor)
            shot_location = all_positions_player.pop(i)
            #shot_location = [int(c) for c in input("\nEnter coordinates, row then column. E.g 2 5:\n").split()]
            # add check for values
            computer.board, hit, computer.lives = player.fire(shot_location[0],shot_location[1], computer.board, computer.lives)
            if hit == False:
                break
            print(f"Here is your shot history to plan your next move: {player.shots_board}")
            if computer.lives == 0:
                break
            
        print("After your turn, your shots fired board looks like this now:\n")
        print(player.shots_board)
        hits = np.count_nonzero(player.shots_board == "X")
        misses = np.count_nonzero(player.shots_board == "*")
        print(f"Total fired shots {hits + misses} with a success rate of {hits / (hits + misses) * 100}\nComputer has {computer.lives} lives left")
        
        # stop game if player lives == 0 
        if computer.lives == 0:
            print(f"Congratulations player {player.id}, you have beaten the computer!")
            break
        
        #print("Computer firing in 3 secs!")
        #sleep(4)
           
        # Computer turn
        # get all positions to not repeat shots to same location
        all_positions_computer = [(x, y) for x in range(10) for y in range(10)]
        while True:
            random_coor = random.choice(all_positions_computer)
            i = all_positions_computer.index(random_coor)
            random_shot = all_positions_computer.pop(i)
            player.board, hit, player.lives = computer.fire(random_shot[0],random_shot[1], player.board, player.lives)
            if hit == False:
                break
            if player.lives == 0:
                break
            
        # stop game if computer lives == 0    
        if player.lives == 0:
            print(f"Unlucky player {player.id}, you have been beaten the computer!")
            break
            
        print("After the computer turn, your board looks like this now:\n")
        print(player.board)
        hits = np.count_nonzero(computer.shots_board == "X")
        misses = np.count_nonzero(computer.shots_board == "*")
        print(f"Total shots on your water: {hits + misses}, with a success rate of {hits / (hits + misses) * 100}.\nYou have {player.lives} lives left")
        
        round += 1
        
        
    print(f"Final boards looked like this, was it close?\nPlayer {player.id} board:\n {player.board} \nComputer board:\n {computer.board}")
    
    
    
if __name__ == "__main__":
    main()
    