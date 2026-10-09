# 1. Logical operators and short-circuit evaluation
# 'or' returns the first truthy value or the last value
print("apple" or "banana")  # 'apple'
print("" or "fallback")      # 'fallback'

# 'and' returns the first falsy value or the last value
print("hello" and 25)        # 25
print([] and "python")       # []

# 2. Comparison operators (==, !=, <, >, <=, >=)
score = 85
is_valid_grade = 70 <= score <= 100  # Chained comparisons
print("Valid grade:", is_valid_grade)

# 3. The 'del' statement removes variable bindings or object items
data = {"a": 1, "b": 2}
del data["a"]
print(data)  # {'b': 2}

temp_var = 100
del temp_var
# print(temp_var)  # Raises NameError