items = ["Jhon", "Erika"]
#- open the file and print
names_list = []

try:
    file = open("names.txt", "r")
    lines = file.readlines()

    for line in lines:
        names_list.append(line.strip())

except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))

print("\nThe original file:")
print(names_list)

#-add 2 new names to the file -------------------------
try:
    file = open("names.txt", 'a')
    for item in items:
        file.write(item + '\n')
except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))
finally:
    file.close()

# open the file again and print it out ----------------

names_list = []

try:
    file = open("names.txt", "r")
    lines = file.readlines()

    for line in lines:
        names_list.append(line.strip())

except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))

print("\nThe modified file:")
print(names_list)


