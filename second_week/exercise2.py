names_dic = {}
clean_names_list = []

# read the txt file------------------------------------
file = open("names.txt", 'r')
names_list = file.readlines()

# strip the \n from each names--------------------------
for name in names_list:
    clean_names_list.append(name.strip())
print("Clean Names List:\n\n", clean_names_list, "\n")

# creat a unique name list------------------------------
uniq_names = set(clean_names_list)
print("Unique names: \n\n",uniq_names,"\n")

# creat a dictionary where the keys are the names from the file and 
# the values are the number of times each name appears in the text file
for uniq_name in uniq_names:
    x = 0
    for name in clean_names_list:
        if uniq_name == name:
            x += 1
    names_dic[uniq_name] = x

print("The asked dictionary:\n\n",names_dic)

# Write out to another file where each line looks like: Name: John, Count: 4

names_dic_keys = names_dic.keys()
names_dic_values = names_dic.values()
i = 0
try:
    file = open("names_dictionary.txt", 'w')
    for i in range(len(names_dic_keys)):
        # file.write("Name: ", names_dic_keys[i], ",", "Count: ", names_dic_values[i],'\n')
        file.write(i, "\n")
except FileNotFoundError as fnfe:
    print('Unable to open file: ' + str(fnfe))
finally:
    file.close()

