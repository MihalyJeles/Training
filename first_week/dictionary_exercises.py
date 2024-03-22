car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'isNew': False
}

car['colour'] = 'blue'
print(car['colour'])

car['model'] = 'Suzuki' 
print(car['model'])

del car['model']
print(car)

for key, value in car.items():
    print(f'key: {key}, value: {value}')
    
