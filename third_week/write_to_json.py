import json

person = {
    "name": {"first": "Rob",
            "second": "Jeles"},
    "phone": 123456
}
# encode & write to a file
with open('example.json', 'w') as f:
    json.dump(person, f)

# read file and decode its content
with open('example.json', 'r') as f:
    my_data = json.load(f)

# git push

print(person["name"]["second"])

x,y = "Misi", "Viki"

print(y)

# r = 5
# b = 4
# print r+b