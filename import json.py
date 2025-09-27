import json


# 1 Convert a Python dictionary into JSON and save it in a file.
data = {
    "id": 101,
    "name": "Sumedh",
    "age": 23,
    "city": "Nashik"
}

# Save dictionary to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent=4 for pretty formatting
print(" Dictionary saved to data.json\n")


# 2 Load data from JSON file and print all values of a specific key.
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("All values of key 'name':", loaded_data["name"], "\n")


# 3 Parse a JSON string of multiple users and print names of users older than 25.
users_json = '''
[
    {"name": "Sumedh", "age": 23},
    {"name": "Bob", "age": 30},
    {"name": "Rahul", "age": 27},
    {"name": "Sam", "age": 20}
]
'''

# Convert JSON string to Python list
users = json.loads(users_json)

print("Users older than 25:")
for user in users:
    if user["age"] > 25:
        print("-", user["name"])
