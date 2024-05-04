import csv

# with open("test.csv") as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(row)

import csv
with open("test.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)