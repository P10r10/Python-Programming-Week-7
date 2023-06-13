import json


def print_persons(filename: str):
    with open(filename) as fp:
        data = fp.read()
    persons = json.loads(data)
    for person in persons:
        hobbies = ", ".join(person["hobbies"])
        print(f"{person['name']} {person['age']} years ({hobbies})")


print_persons("file1.json")
print_persons("file2.json")
print_persons("file3.json")
print_persons("file4.json")
