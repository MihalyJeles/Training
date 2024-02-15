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

stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    for x in stuff:
        print (stuff[x + 1])
except:
    print ('Something went wrong!')