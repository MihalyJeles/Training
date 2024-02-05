## Part 1

### Strings

# first_name = "Mihaly"
# print(f'My first name is {first_name}')
# second_name = "Jeles "
# full_name = first_name + " " + second_name
# print(f'My full name is {full_name}.')
# ------------------------------------------
# Integers

# a = 10
# b = 15
# c = a * b + 10
# print(c)
# print(f'The product of {a} and {b} is {c}')
# ------------------------------------------
# Lists
# people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# third_element = people[2]
# print(f'Third element of the list is {third_element}')

# third_element_from_back = people[-5]
# print(f'Third element of the list from the back is {third_element_from_back}')

# split_list = people[2:6]
# print(split_list)

# if people[0] == people[6]:
#     print(f'The first {people[0]} and the last {people[6]} element are equal!')
# else:
#     print(f'The first {people[0]} and the last {people[6]} element are not equal!')
# ------------------------------------------
### Input

# first_name = input(f'Please give me your first name: ')
# second_name = input(f'Please give me your second name: ')
# full_name = first_name + " " + second_name
# print(full_name)

# x = int(input(f'Give me x: '))
# y = int(input(f'Give me y: '))
# if x == y:
#     print("True")
# else:
#     print("False")
# ------------------------------------------
## Part 2

### Input and Numbers
# number = int(input("Please give me a number: "))
# if number % 4 == 0:
#     print("The number is even and multiple of 4!")
# elif number % 2 == 0:
#     print("The number is even!")
# else:
#     print("The number is odd!")

# number = int(input("Please give me a number: "))
# if number % 5 == 0 and number % 3 == 0:
#     print("buzz and fizz")
# elif number % 5 == 0:
#     print("buzz")
# elif number % 3 == 0:
#     print("fizz")

### Temperature Conversion

# temperature_type = ""
# number = 0
# c = ""
# while c != "good":
#     temperature_type = input("Please give me the temprature type ('f' = fahrenheit / 'c' = celsius): ")
#     if temperature_type == "c" or "C" or "f" or "F":
#         c == "good"
#     else:
#         print("Wrong input!")


temperature_type = input("Please give me the temperature type ('f' = fahrenheit / 'c' = celsius): ")

number = int(input("Please give me the temperature: "))

if temperature_type == "f" or temperature_type == "F":
    converted_number = (number * 1.8) + 32
    print(f'{number} celsius = {converted_number} fahrenheit')
elif temperature_type == "c" or temperature_type == "C":
    converted_number = (number - 32) * (5/9)
    print(f'{number} fahrenheit = {converted_number} celsius')
else:
    print("Wrong input!")

