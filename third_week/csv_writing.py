import csv
with open('test.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Joe', 'Bloggs', 40])
    writer.writerow(['Jane', 'Smith', 50])