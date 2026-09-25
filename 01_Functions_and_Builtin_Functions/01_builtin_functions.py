"""
01_builtin_functions.py
Overview of core Python built-in functions, basic definition syntax, and type inspection.
"""

# 1. Calling a built-in function
print("Hello, Python!")

# 2. Inspecting the function object itself
print(print)  # Output: <built-in function print>

# 3. Object type and memory address inspection
name = "Paayas"
print("Type:", type(name))  # <class 'str'>
print("Memory ID:", id(name))  # Unique memory address integer

# 4. Working with sequences (strings, lists)
numbers = [10, 20, 5, 45, 30]
print("Length:", len(numbers))  # 5
print("Sum:", sum(numbers))      # 110
print("Min:", min(numbers))      # 5
print("Max:", max(numbers))      # 45

# 5. Rounding numbers
float_val = 14.678
print("Rounded:", round(float_val))     # 15
print("Rounded to 2 dec:", round(float_val, 2))  # 14.68

# 6. Type conversion (Type Casting)
num_str = "120"
num_int = int(num_str)
print("Converted:", num_int, type(num_int))

# 7. Basic Function Definition syntax preview
def my_fn(a, b):
    c = a + b
    return c

result = my_fn(10, 25)
print("Custom function result:", result)