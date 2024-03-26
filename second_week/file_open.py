# read the whole file

# file = open("my_file.txt", "r")

# contents = file.read()
# print(contents)

# read the file line by line

# people.py
# file = open("my_file.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line) 

# read the file's lines and add them to a list

names_list = []

try:
    file = open("names.txt", "r")
    lines = file.readlines()

    for line in lines:
        names_list.append(line.strip())

except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))


print(names_list)



