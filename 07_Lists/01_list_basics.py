# Lists are ordered, mutable collections of items
fruits = ["apple", "banana", "cherry"]

# Indexing and slicing
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'cherry'
print(fruits[0:2])  # ['apple', 'banana']

# Mutating in-place (lists are mutable, unlike strings)
fruits[1] = "blueberry"
print(fruits)       # ['apple', 'blueberry', 'cherry']

# Length and membership
print(len(fruits))          # 3
print("apple" in fruits)    # True