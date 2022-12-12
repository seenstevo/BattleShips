boats = {"B1": 1, "B2": 1, "B3": 1, "B4": 1, 
         "B5": 2, "B6": 2, "B7": 2,
         "B8": 3, "B9": 3,
         "B10": 4}

board_dimensions = (10, 10)

lives = sum(boats.values())

while board_dimensions[0] * board_dimensions[1] <= (lives + 5):
    board_dimensions = (board_dimensions[0] + 1, board_dimensions[1] + 1)

water_sym = " "
boat_sym = "O"
hit_water_sym = "*"
hit_boat_sym = "X"

#print(board_dimensions, lives)