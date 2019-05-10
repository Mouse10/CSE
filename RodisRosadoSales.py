import csv

with open("Sales Records.csv",  "r") as new_csv:
    reader = csv.reader(new_csv)
    total_fruits = 0
    total_cosmetics = 0
    total_snacks = 0
    clothes = 0
    office_supplies = 0
    vegetables = 0
    baby_food = 0
    meat = 0
    breverages = 0
    personal_care = 0
    house_hold = 0
    cereal = 0

    for row in reader:
        old_number = row[13]
        region = row[0]
        item = row[2]
        if item == "Fruits":
            total_fruits = total_fruits + float(old_number)
        if item == "cosmetics":
            total_cosmetics = total_cosmetics + float(old_number)
        if item == "snacks":
            total_snacks = total_snacks + float(old_number)
        if item == "clothes":
            clothes = clothes + float(old_number)
        if item == "office_supplies":
            office_supplies = office_supplies + float(old_number)
        if item == "vegetables":
                vegetables = vegetables + float(old_number)
        if item == "baby_food":
                baby_food = baby_food + float(old_number)
        if item == "meat":
                meat = meat + float(old_number)
        if item == "breverages":
                breverages + float(old_number)




print("You are making %s in profit" % (total_cosmetics))
print("You are making %s in profit" % (total_fruits))
print("You are making %s in profit for selling snacks" % (total_snacks))