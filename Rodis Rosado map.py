edison_map = {
    "R19A": {
        "NAME": "Mr. Wibe's room",
        "DESCRIPTION": "This is the room that you are in.",
        "PATHS": {
            "NORTH": "PARKING_LOT",
            "EAST": "W_BUILDING",
            "WEST": "NORTH_ADMIN",
            "SOUTH": "CAFETERIA_FOOD",
        }
    },
    "PARKING_LOT": {
        "NAME": "A Parking lot",
        "DESCRIPTION": "There are a few cars parked here.",
        "PATHS": {
            "SOUTH": "W_BUILDING",
            "NORTH": "PARKING_LOT",
            "WEST": "NORTH_ADMIN",
        }
    },
    "W_BUILDING": {
        "NAME": "Main Building",
        "DESCRIPTION": "This building has 29 classrooms.",
        "PATHS": {
            "SOUTH": "SCIENCE_ROOM",
            "NORTH": "PARKING_LOT",
        }
    },
    "SCIENCE_ROOM": {
        "NAME": "SCIENCE.",
        "DESCRIPTION": "This room is the science room.",
        "PATHS": {
            "EAST": "BUS_LANE",
            "NORTH": "W_BUILDING",
        }
    },
    "SOUTH_ADMIN": {
        "NAME": "COUNSELING.",
        "DESCRIPTION": "This is where bad kids go.",
        "PATHS": {
            "NORTH": "W_BUILDING",
            "WEST": "SWIMMING_POOL"
        }
    },
    "SWIMMING_POOL": {
        "NAME": "Pool",
        "DESCRIPTION": "This is the pool",
        "PATHS": {
            "EAST": "SOUTH_ADMIN",
            "NORTH": "CAFETERIA_FOOD",
        }
    },
    "CAFETERIA_FOOD": {
        "NAME": "Cafeteria",
        "DESCRIPTION": "This is where you get food",
        "PATHS": {
            "NORTH": "R1A9",
            "EAST": "SCIENCE_ROOM",
            "WEST": "GYM",

        }
    },
    "GYM": {
        "NAME": "Gymnasium",
        "DESCRIPTION": "This is where you work out",
        "PATHS": {
            "EAST": "SCIENCE_ROOM",
            "NORTH": "R19A",
            "SOUTH": "SWIMMING POOL"
        }
    },
    "NORTH_ADMIN": {
       "NAME": "North admin",
        "DESCRIPTION": "This is where you come if you are late",
        "PATHS": {
            "WEST": "GYM",
            "EAST": "LIBRARY"
        }
    },
    "LIBRAY": {
        "NAME": "LIBRAY",
        "DESCRIPTION": "This is where you get books",
        "PATHS": {
            "WEST": "NORTH_ADMIN",
            "SOUTH": "CAFETERIA_FOOD",
            "EAST": "R19A"
            # 10 rooms
        }
    }
}
#
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = edison_map["R19A"]
playing = True



while playing:
    print(current_node["NAME"])
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = edison_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")

