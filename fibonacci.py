# The fibonacci sequence is the sum of the previous two values
# 1, 1, 2, 3, 5, 8, 13...

position = int(input('Please give me the position of the number from the sequence, what you would like to know!: '))
# fib
# def fibonacci(position):
#     i = 1
#     while i < position:

def fib(position):
    if position < 2:
        return 1
    return fib(position-2) + fib(position-1) 

print(f'Position: {position}')
print(fib(position))