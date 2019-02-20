class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east

# these are the instances of the rooms (INSTANTIATION)

# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking lot", None, R19A)


R19A.north = parking_lot

# Option 2 - Use strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("The Parking loot", None, "R19A")