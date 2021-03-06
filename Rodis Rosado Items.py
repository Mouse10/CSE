class Item(object):
    def __init__(self, name):
        self.name = name

class Plane(Item):
    def __init__(self, name, wheels, wings, frame, engine, window, landing_lights,
                 toilet, seat, luggage, scanner, fuel, fire_extinguisher, tv):
        super(Plane, self).__init__(name)
        self.wheels = wheels
        self.wings = wings
        self.frame = frame
        self.engine = engine
        self.window = window
        self.landing_lights = landing_lights
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
    def __init__(self, gauze, bandages, tweezers,scissors, gloves, tape, ice_pack, gel):
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

class Baseball_cabnet(Item):
    def __init__(self, shovel, bats, gloves, helmet, cleats, baseball, bases, hats):
        super(Baseball_cabnet, self).__init__("name")
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
        super(Golfcart, self).__init__("name")
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
    def __int__(self, screen, battery, usb, beyboard):
        super(Laptop, self).__int__("name")
        self.screen = screen
        self.battery = battery
        self.usb = usb
        self.keyboard = keyboard

class Projector(Item):
    def __int__(self):
        super(Projector, self).__int__("name")
        self.light_bulb = bulb
        self.buttons = button
        self.frame = frame

class Refrigerator(Item):
    def __int__(self, dispenser, compressor, refrigerant):
        super(Refrigerator, self).__int__("name")
        self.door = door
        self.ice_dispenser = dispenser
        self.compressor = compressor
        self.refrigerant = refrigerant

class Microwave(Item):
    def __int__(self, magnetron, electricity, capacitor):
        super(Microwave, self).__int__("name")
        self.magnetron = magnetron
        self.electricity = electricity
        self.capacitor = capacitor

class Car(object):
    def __init__(self, turning, speed_measurement, fuel_measurement,
                 revolutions_per_minute, battery_measurement, wheels):
        self.steering_wheel = turning
        self.speedometer = speed_measurement
        self.fuel_gauge = fuel_measurement
        self.rpm = revolutions_per_minute
        self.battery_gauge = battery_measurement
        self.wheels = wheels