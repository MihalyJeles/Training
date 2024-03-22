# for x in range(0,11):
#     print(x)

# x = 0
# while x < 11:
#     print(x)
#     x += 1

# nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]

# for x in nums:
#     print(x)

# for x in range(0,11):
#     print(x)
# else:
#     print('Done')

# list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
# list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

# for x in list1:
#     for y in list2:
#         if x == y:
#             print(x)

# infinity while loop
import random

while True:
    x = random.randint(1,100)
    print(f'The generated number is: {x}')
    if x % 5 == 0:
        print(f'The loop breaked before the program exits, because {x} multiple of 5!')
        break
    elif x % 3 == 0:
        print(f'The iteration is skipped,because {x} multiple of 3!')
        continue
    else:
        print('The number is:', x)