# 1. Booleans (bool)
is_valid = True
is_empty = False

# 2. Comparison expressions returning booleans
print(10 > 5)   # True
print(20 == 20) # True
print(15 <= 8)  # False

# 3. Truthy and Falsy values with bool()
# Falsy: 0, 0.0, "", None, [], {}, set()
print(bool(0))        # False
print(bool(""))       # False
print(bool(None))     # False

# Truthy: Any non-zero number or non-empty sequence
print(bool(42))       # True
print(bool("text"))   # True