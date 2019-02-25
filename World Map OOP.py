class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west


# these are the instances of the rooms (INSTANTIATION)

R19A = Room("Mr. Wiebe's Room", 'parking_lot', "cafeteria_food", "w_building")
parking_lot = Room("The Parking lot", None, "R19A")
w_building = Room("w_building", "parking_lot", "science_room", "None", "None")
cafeteria_food = Room("cafeteria_food", "R19A", "None", "science_room", "gym")
north_admin = Room("north_admin", "w_building", "None", "None", "swimming_pool")
swimming_pool = Room("swimming_pool", "cafeteria_food", "None", "south_admin", "None")
science_room = Room("science_room", "w_building", "south_admin", "None", "cafeteria_food")
south_admin = Room("south_admin", "science_room", "None", "None", "swimming_pool")
gym = Room("gym", "R19A", "swimming_pool", "science_room", "None")
libray = Room("libray", "None", "cafeteria", "R19A", "north_admin")
