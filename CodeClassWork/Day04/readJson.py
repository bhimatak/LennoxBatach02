import json

d1 = dict()
print(id(d1))
with open("test.json", "r") as file:
    data = json.load(file)
    d1 = data

    print(data, type(data))
    print(id(d1))

print(d1, id(d1))