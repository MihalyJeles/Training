# Python 2 Exercises

## Functions

# def sum(a,b):
#     return a+b

# print(sum(4,5))

# def sum(*numbers): 
#     result = 0
#     for num in numbers:
#         result += num
#     return result

# x = sum(4,5,8,9,3,7)
# print(x)

def names_dictionary(**names):
    result = ""
    for name in names.values():
        result += name
    # print(result)
    return result

print(names_dictionary(a = 'Mihaly', b = 'Viktoria', c = 'Emma', d = 'Dominik'))