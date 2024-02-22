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

list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for x in list1:
    for y in list2:
        if x == y:
            print(x)