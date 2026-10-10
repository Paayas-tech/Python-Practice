# 1. Iterating through lists, tuples, and strings
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

for char in "Data":
    print("Char:", char)

# 2. Iterating with range()
for i in range(1, 4):
    print(f"Count: {i}")

# 3. Iterating through dictionaries (.keys(), .values(), .items())
user = {"name": "Paayas", "role": "Data Analyst", "city": "Delhi"}

for key in user:
    print("Key:", key)

for key, value in user.items():
    print(f"{key} -> {value}")

# 4. Sets iteration (unordered, unique)
tags = {"python", "sql", "analytics"}
for tag in tags:
    print("Tag:", tag)