people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

try:
    file = open("exercise.txt", 'w')
    for person in people:
        file.write(person + '\n')
except FileNotFoundError as e:
    print("Unable to open file: "+ str(e))
finally:
    file.close()