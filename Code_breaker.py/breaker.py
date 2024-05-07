names_list = []
try:
    file = open("code.txt", "r")
    lines = file.readlines()
    for line in lines:
        names_list.append(line.strip())
except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))

code = int(names_list[0])

breaking_code = 0000

if breaking_code == code:
    print("This is your code: " + code)
else:
    breaking_code += breaking_code


