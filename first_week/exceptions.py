# try:
#     x = 1 / 0
# except:
#     print("You can't do that!")
#     print("We can still run the program after this though")


# number = int(input(f'Please give me your age: '))

# try:
#     if number > 100:
#         print('The number is bigger than 100!')
#     elif number > 50 and number < 100:
#         print('The number is between 50 and 100!')
# except:
#     print('Please give me a number!')

# stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# try:
#     for x in stuff:
#         print (stuff[x + 1])
# except:
#     print ('Something went wrong!')

# try:
#     x = 1 / 0
# except Exception as e:
#     print(e)

number = int(input(f'Please give a number: '))
try:
    print(f'100 / The given number is = ',100/number)
except Exception as e:
    print(f'This is an exception because {e} is not possible!')
