class Car(object):
    def __init__(self, turning, speed_measurement, fuel_measurement, revolutions_per_minute, battery_measurement):
        self.steering_wheel = turning
        self.speedometer = speed_measurement
        self.fuel_gauge = fuel_measurement
        self.rpm = revolutions_per_minute
        self.battery_gauge = battery_measurement
        self.functioning = True

    def charge(self, time):
            if self.functioning:
                # Computer is already charged
                if self.battery_gauge >= 100:
                    print("The car is already filled.")
                    return
                else:
                    print("The computer is now at %d%% " % self.battery_left)
            else:
                    print("It's broken. Good job.")

    def smash(self):
        self.functioning = False
        print("I took the Car...")
        print()
        print()
        print()
        print("...And I THREW IT ON THE GROUND!!!!!")
