# def outer_function():
#     b = 20
#     def inner_func():
#         c = 30
# a = 10

x = 300
def myfunc():
    x = 200
    print(x) # 1
myfunc()
print(x) # 2