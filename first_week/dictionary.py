car = {
    # key # value
    'make': 'Jaguar',
    'model': 'XF',
    'year' : 2019,
    'isNew': False
}
print (car['make'], car['year'])
for x in car:
    print (car[x])

car['colour'] = 'Red'
print(car)

car['colour'] = 'Blue'
print(car)

del car['colour']
print(car)

print(car['year'])

print(car.get(x))

print(car.items())

print(car.keys())

print(car.values())

print('colour' in car)

car['colour'] = 'Red'

print('colour' in car)

print( len(car))

fruit = {
    'type': 'apple',
    'color': 'green'
}

fruit_color = fruit['color']
print(fruit_color)


# d = {
#     'a': 'b',
#     1: 'c',
#     0.75: 'test',
#     'd': [1, 2, 3],
#     'e': { 'f': 'g' }
# }

# print(d)

