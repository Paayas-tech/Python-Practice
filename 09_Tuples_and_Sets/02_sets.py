# Sets are unordered collections of unique elements (no duplicates)
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)  # Duplicates removed: {'apple', 'banana', 'cherry'}

# Adding and removing elements
fruits.add("orange")
fruits.discard("banana")  # .discard() avoids KeyError if element is absent
print(fruits)

# De-duplicating a list using set()
raw_ids = [101, 102, 101, 103, 102]
unique_ids = list(set(raw_ids))
print("Unique IDs:", unique_ids)