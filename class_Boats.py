class Boat:
    
    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates
        self.boat_list = ["O"] * size
        
        
    def update_boat(self, size):
        pass
        
        
        
        
test_boat = Boat(4, ((2,6), (3,6), (4,6),(5,6)))

print(test_boat)