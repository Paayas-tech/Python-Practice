# Tuples are ordered, immutable collections (defined with parentheses)
point = (10, 20)
user_info = ("Paayas", 22, "Analyst")

# Indexing and slicing work like lists
print(point[0])        # 10
print(user_info[1:])   # (22, 'Analyst')

# Immutability: point[0] = 15 raises TypeError

# Tuple unpacking
x, y = point
print(f"x: {x}, y: {y}")

# Methods: .count() and .index()
nums = (1, 2, 3, 2, 2)
print("Count of 2:", nums.count(2))  # 3
print("Index of 3:", nums.index(3))  # 2