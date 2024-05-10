import csv
# with open('test.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(['Joe', 'Bloggs', 40])
#     writer.writerow(['Jane', 'Smith', 50])

with open('test.csv', mode='w') as file:
    fieldnames = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
    'first_name': 'Jan',
    'last_name': 'Smith',
    'age': 60
    })
    writer.writerow({
    'first_name': 'Jhon',
    'last_name': 'Norb',
    'age': 50
    })
    writer.writerow({
    'first_name': 'Bob',
    'last_name': 'High',
    'age': 26
    })
