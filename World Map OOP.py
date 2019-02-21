class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None,):
        self.name = name
        self.north = north
        self.south = south
        self.east = east


# these are the instances of the rooms (INSTANTIATION)

R19A = Room("Mr. Wiebe's Room", 'parking_lot', "cafeteria_food", "w_building")
parking_lot = Room("The Parking lot", None, "R19A")
w_building = Room("w_building", "parking_lot", "science", "None", "None")
cafeteria_food = Room("cafeteria_food", "R19A", "None", "science", "gym")
north_admin = Room("")