# 1. Common built-in functions for sequences (strings, lists, tuples)
numbers = [15, 3, 27, 8]
print(len(numbers))   # Length: 4
print(min(numbers))   # Minimum: 3
print(max(numbers))   # Maximum: 27
print(sum(numbers))   # Sum: 53

# 2. Pairing sequences with zip()
headers = ["id", "tool", "category"]
data = [1, "Python", "Language"]

zipped = zip(headers, data)
print(list(zipped))  # [('id', 1), ('tool', 'Python'), ('category', 'Language')]

# 3. Converting a zip object directly to a dictionary (Lecture 80)
zipped_dict = dict(zip(headers, data))
print(zipped_dict)   # {'id': 1, 'tool': 'Python', 'category': 'Language'}