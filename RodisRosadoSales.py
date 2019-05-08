import csv

with open("Sales Records.csv",  "r") as new_csv:
    reader = csv.reader(new_csv)

    for row in reader:
        old_number = row[13]
        print(old_number)
