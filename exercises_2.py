# for x in [0,1,2]:
#     print(f'current number is {x}')

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# for x in range(0, 3):
#     print(f'current number is {x}')

# adjectives = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for adj in adjectives:
#     for fruit in fruits:
#         if fruit == "cherry":
#             break
#         print(adj, fruit)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     if fruit == "banana":
#         continue
#     print(fruit)




# Python 2 Exercises

## Loops

# for x in range(0, 11):
#     print(x)

# x = 0
# while x<11:
#     print(x)
#     x += 1

# nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]
# for x in nums:
#     print(x)
    
# for x in range(0,11):
#     print(x)
# else:
#     print("Done!")

# list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
# list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

# for x in list1:
#     for y in list2:
#         if x == y:
#             print(x)

import random

number = 0
while number < 2:
    x = random.randint(1,100)
    if x % 5 == 0:
        print(f"Happened before the program exits!Because {x} is multiplie of 5")
        break
    elif x % 3 == 0:
        print(f"Skipped!Because {x} is multiplie of 3")
        continue
    else:
        print(x)