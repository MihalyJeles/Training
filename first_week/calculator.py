# basic calculator
import os

# clear screen function
def Clear_screen():
    os.system('cls')

# press enter to continue
def press_to_continue():
    input('\nPress enter to continue!')

def sum(number, next_number):
    result = 0
    result = number + next_number
    return result

def subtraction(number, next_number):
    result = 0
    result = number - next_number
    return result

def divide(number, next_number):
    result = 0
    result = number / next_number
    return result

def multiplication(number, next_number):
    result = 0
    result = number * next_number
    return result

function = ''

while function not in ('+','-','/','*'):
    print('\nThis is a basic calculator!\n')
    print('Please give me the numbers and the right functions between them!\n')
    print('''The following functions are available:
        (+) -sum
        (-) -subtraction
        (/) -divide
        (*) -multiplication
        ''')

    print('\nThe calculator is running:\n')
    number = int(input('Please give me the number: '))
    function = input('Please give me the choosen function: ')
    next_number = int(input('Please give me the next number: '))

    if function == '+':
        print(f'{number} {function} {next_number} = {sum(number, next_number)}')
    elif function == '-':
        print(f'{number} {function} {next_number} = {subtraction(number, next_number)}')
    elif function == '/':
        print(f'{number} {function} {next_number} = {divide(number, next_number)}')
    elif function == '*':
        print(f'{number} {function} {next_number} = {multiplication(number, next_number)}')
    else:
        print(f'{function} is not available function!')
        print('Please give me a function from the available options!')
        press_to_continue()
        Clear_screen()

