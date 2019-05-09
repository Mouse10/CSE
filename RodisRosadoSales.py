import csv

with open("Sales Records.csv",  "r") as new_csv:
    reader = csv.reader(new_csv)
    total = 0
    for row in reader:
        old_number = row[13]
        region = row[0]
        item = row[2]
        if item == "Fruits":
            print(old_number)
            total = total + float(old_number)

print(total)