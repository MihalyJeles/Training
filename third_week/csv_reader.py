import csv

with open("test.csv") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)
