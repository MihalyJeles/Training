def add_numbers(a, b):
    return a + b

print(add_numbers(5,4))

def get_name():
    return 'Alice'

print(get_name())

# def my_function(a, b, c):
#     print(a, b, c)

# my_function('hello', 'world', '!')

# def my_function(a, b, c='!'):
#     print(a, b, c)

# my_function('hello', 'world')

# my_function('hello', 'world', '?')

def my_function(*people):
    for person in people:
        print(person)

my_function("Alice", "Bob", "John")

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    print (result)
concatenate(a="Real", b="Python", c="Is", d="Great", e="!")



luxury_cars = ['Ferrari', 'Lamborghini', 'Tractor', 'Porsche']
print(luxury_cars)
del luxury_cars[2]
print(luxury_cars)




