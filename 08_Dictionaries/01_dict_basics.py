# Dictionaries store data in key-value pairs (keys must be immutable, e.g., str/int)
user = {
    "name": "Paayas",
    "role": "Data Analyst",
    "experience_years": 1
}

# Accessing values
print(user["name"])  # 'Paayas'

# Modifying and adding keys
user["experience_years"] = 2       # Updating existing key
user["tools"] = ["Python", "SQL"]  # Adding a new key
print(user)

# Deleting keys
del user["role"]
print(user)

# Converting a list of paired tuples to a dict (Lecture 63)
pairs = [("id", 101), ("status", "active")]
status_dict = dict(pairs)
print(status_dict)