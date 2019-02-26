class Room(object):
    # This is a constructor
    def __init__(self, name, north=None, south=None, east=None, west=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A string (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]

# these are the instances of the rooms (INSTANTIATION)


R19A = Room("Mr. Wiebe's Room", 'parking_lot', "cafeteria_food", "w_building", "library")
parking_lot = Room("The Parking lot", None, "R19A")
w_building = Room("w_building", "parking_lot", "science_room", "None", "None")
cafeteria_food = Room("cafeteria_food", "R19A", "None", "science_room", "gym")
north_admin = Room("north_admin", "w_building", "None", "None", "swimming_pool")
swimming_pool = Room("swimming_pool", "cafeteria_food", "None", "south_admin", "None")
science_room = Room("science_room", "w_building", "south_admin", "None", "cafeteria_food")
south_admin = Room("south_admin", "science_room", "None", "None", "swimming_pool")
gym = Room("gym", "R19A", "swimming_pool", "science_room", "None")
library = Room("library", "None", "cafeteria", "R19A", "north_admin")

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)


    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command in directions:
        try:
           next_room = player.find_room(command)
           player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")

