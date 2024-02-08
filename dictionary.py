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

d = {
    'a': 'b',
    1: 'c',
    0.75: 'test',
    'd': [1, 2, 3],
    'e': { 'f': 'g' }
}

print(d)