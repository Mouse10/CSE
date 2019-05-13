class Item(object):
    def __init__(self, name):
        self.name = name


class Room(object):
    # This is a constructor :)
    def __init__(self, name, north=None, south=None, east=None, west=None, description=None, item=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.item = item


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


class Item(object):
    def __init__(self, name):
        self.name = name


class Plane(Item):
    def __init__(self, name, wheels, wings, frame, engine, window,
                 toilet, seat, luggage, scanner, fuel, fire_extinguisher, tv):
        super(Plane, self).__init__("Plane")
        self.wheels = wheels
        self.wings = wings
        self.frame = frame
        self.engine = engine
        self.window = window
        self.toilet = toilet
        self.seats = seat
        self.luggage = luggage
        self.scanner = scanner
        self.fuel = fuel
        self.fire_extinguisher = fire_extinguisher
        self.tv = tv


class Mre(Item):
    def __init__(self, crackers, tea, cheese, gum, beef_taco, beef_stew, spoon, matches):
        super(Mre, self).__init__("Meal - Ready to Eat")
        self.crackers = crackers
        self.tea = tea
        self.cheese = cheese
        self.gum = gum
        self.beef_taco = beef_taco
        self.beef_stew = beef_stew
        self.spoon = spoon
        self.matches = matches


class Iphone8(Item):
    def __init__(self, battery, storage, finger_print, gyroscope, accelerometer, barometer):
        super(Iphone8, self).__init__("Iphone 8 plus")
        self.battery = battery
        self.storage = storage
        self.fingerprint = finger_print
        self.gyroscope = gyroscope
        self.accelerometer = accelerometer
        self.barometer = barometer


class FirstAid(Item):
    def __init__(self, gauze, bandages, tweezers, scissors, gloves, tape, ice_pack, gel):
        super(FirstAid, self).__init__("First Aid Kit")
        self.gauze = gauze
        self.bandages = bandages
        self.tweezers = tweezers
        self.scissors = scissors
        self.gloves = gloves
        self.tape = tape
        self.ice_pack = ice_pack
        self.gel = gel


class Library(Item):
    def __init__(self, books, computers, tables, pencils, chairs):
        super(Library, self).__init__("Library")
        self.books = books
        self.computers = computers
        self.tables = tables
        self.pencils = pencils
        self.chairs = chairs


class Baseball_box(Item):
    def __init__(self, shovel, bats, gloves, helmet, cleats, baseball, bases, hats):
        super(Baseball_box, self).__init__("Box full of Baseball equipment")
        self.shovel = shovel
        self.bats = bats
        self.gloves = gloves
        self.helmets = helmet
        self.cleats = cleats
        self.baseball = baseball
        self.bases = bases
        self.hats = hats


class Golfcart(Item):
    def __init__(self, battery, wheels, seats, wind_shield, horn):
        super(Golfcart, self).__init__("Golfcart")
        self.battery = battery
        self.wheels = wheels
        self.seats = seats
        self.windshield = wind_shield
        self.horn = horn


class Fire_ax(Item):
    def __init__(self, blade, handle):
        super(Fire_ax, self).__init__("Fire Ax")
        self.blade = blade
        self.wood_handle = handle


class Laptop(Item):
    def __init__(self, screen, battery, usb, keyboard):
        super(Laptop, self).__init__("Laptop")
        self.screen = screen
        self.battery = battery
        self.usb = usb
        self.keyboard = keyboard


class Projector(Item):
    def __int__(self):
        super(Projector, self).__init__("Projector")
        self.light_bulb = bulb
        self.buttons = button
        self.frame = frame


class Refrigerator(Item):
    def __int__(self, dispenser, compressor, refrigerant):
        super(Refrigerator, self).__init__("Refrigerator")
        self.door = door
        self.ice_dispenser = dispenser
        self.compressor = compressor
        self.refrigerant = refrigerant


class Microwave(Item):
    def __int__(self, magnetron, electricity, capacitor):
        super(Microwave, self).__init__("Microwave")
        self.magnetron = magnetron
        self.electricity = electricity
        self.capacitor = capacitor


class Car(Item):
    def __init__(self, turning, speed_measurement, fuel_measurement, revolutions_per_minute, battery_measurement, wheels):
        super(Car, self).__init__("Car")
        self.steering_wheel = turning
        self.speedometer = speed_measurement
        self.fuel_gauge = fuel_measurement
        self.rpm = revolutions_per_minute
        self.battery_gauge = battery_measurement
        self.wheels = wheels


R19A = Room("Mr. Wiebe's Room", 'parking_lot', "cafeteria_food", "w_building", "library",
            "This is where Mr. Wiebe teaches", Laptop("Laptop", "5800 mAh", "4 ports", 1))
parking_lot = Room("The Parking lot", None, "R19A", None, None, "This is where the teachers park", Plane("Plane", 16, 5, 1, 4, 250, 1, 250, 100, 3, 150000, 10, 200))
w_building = Room("w_building", "parking_lot", "science_room", None, None, "This building has english and spanish", None)
cafeteria_food = Room("cafeteria_food", "R19A", None, "science_room", "gym", None, Mre(1, 3, 2, 4, 3, 2, 2, 10))
north_admin = Room("north_admin", "w_building", None, None, "swimming_pool", None, Golfcart("electric_battery", 4, 5, 1, 1))
swimming_pool = Room("swimming_pool", "cafeteria_food", None, "south_admin", None, None, Iphone8("2675mAh", "64GB", 1, 1, 1, 1))
science_room = Room("science_room", "w_building", "south_admin", None, "cafeteria_food", None, Refrigerator(0))
south_admin = Room("south_admin", "science_room", None, None, "swimming_pool", None,
                   Car(180, "120mph", "55_liters", "7000_rpm", "6yrs", 4))
gym = Room("gym", "R19sA", "swimming_pool", "science_room", None, None, Baseball_box(3, 11, 20, 10, 10, 30, 4, 25))
library = Room("library", None, "cafeteria", "R19A", "north_admin",
               "This is where you can get books and use computers", Fire_ax(1, 1))

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True
short_directions = ['n', 's', 'e', 'w']

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    if player.current_location.item is not None:
        print("There is a %s here" % player.current_location.item.name)
    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command in directions:

        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
            elif " take " in command:
                item_name = command[5:]
    found_item = None
    if player.current_location.item.name == item_name:
            found_item = player.current_location.item

    if found_item is not None:
            player.inventory.append(found_item)

            player.current_location.item = None
        print("You have taken this %s in this room" % item_name)
            else:
        print("Command not recognized.")