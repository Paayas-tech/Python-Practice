# 1. Basic tuple/list unpacking
point = (10, 20)
x, y = point
print(f"x: {x}, y: {y}")

# 2. Unpacking a list of tuples in a loop
users = [("Alice", 25), ("Bob", 30)]
for name, age in users:
    print(f"{name} is {age} years old")

# 3. Extended unpacking using the * operator (gathering remaining elements)
numbers = [1, 2, 3, 4, 5, 6]
first, second, *rest = numbers
print(first)   # 1
print(second)  # 2
print(rest)    # [3, 4, 5, 6] (always packed as a list)

# Unpacking middle elements
start, *middle, end = numbers
print("Start:", start, "| Middle:", middle, "| End:", end)