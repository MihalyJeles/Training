# Python 2 Exercises

## Functions

# def sum(a,b):
#     return a+b

# print(sum(4,5))

def sum(*numbers): 
    result = 0
    for num in numbers:
        result += num
    return result

x = sum(4,5,8,9,3,7)
print(x)