from collections import defaultdict

people = [
    {"name": "Alice", "age": 30, "occupation": "engineer"},
    {"name": "Bob", "age": 28, "occupation": "doctor"},
    {"name": "Charlie", "age": 35, "occupation": "engineer"},
    {"name": "David", "age": 22, "occupation": "doctor"},
    {"name": "Eve", "age": 29, "occupation": "artist"}
]

# Creating a defaultdict to automatically initialize an empty list for each occupation
occupation_dict = defaultdict(list)

# Populating the dictionary
for person in people:
    occupation_dict[person['occupation']].append(person['name'])

# Converting the defaultdict to a regular dictionary
result_dict = dict(occupation_dict)

print(result_dict)

