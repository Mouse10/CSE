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
        if item == "Cosmetics":
            total_cosmetics = total_cosmetics + float(old_number)
        if item == "Snacks":
            total_snacks = total_snacks + float(old_number)
        if item == "Clothes":
            clothes = clothes + float(old_number)
        if item == "Office Supplies":
            office_supplies = office_supplies + float(old_number)
        if item == "Vegetables":
            vegetables = vegetables + float(old_number)
        if item == "Baby Food":
            baby_food = baby_food + float(old_number)
        if item == "Meat":
            meat = meat + float(old_number)
        if item == "Beverages":
            breverages = breverages + float(old_number)
        if item == "Personal Care":
            personal_care = personal_care + float(old_number)
        if item == "Household":
            house_hold = house_hold + float(old_number)
        if item == "Cereal":
            cereal = cereal + float(old_number)
        if item(item) > item:
            print(item)

profit_list = [total_snacks, total_cosmetics, total_fruits, clothes, ]


print("You are making %s in profit for selling cosmetics" % (total_cosmetics))
print("You are making %s in profit for selling fruits" % (total_fruits))
print("You are making %s in profit for selling snacks" % (total_snacks))
print("You are making %s in profit for selling clothes" % (clothes))
print("You are making %s in profit for selling office supplies" % (office_supplies))
print("You are making %s in profit for selling vegetables" % (vegetables))
print("You are making %s in profit for selling baby food" % (baby_food))
print("You are making %s in profit for selling meat" % (meat))
print("You are making %s in profit for selling breverages" % (breverages))
print("You are making %s in profit for selling personal care" % (personal_care))
print("You are making %s in profit for selling house hold items" % (house_hold))
print("You are making %s in profit for selling cereal" % (cereal))
