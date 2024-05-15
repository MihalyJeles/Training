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

print(my_data)
print(person["name"])
inside_dictionary = person["name"]
print(inside_dictionary["second"])
print(person["name"]["second"])