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

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

