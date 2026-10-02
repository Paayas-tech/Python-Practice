# 1. Assignment creates a reference (NOT a copy)
original = [1, 2, 3]
reference = original
reference.append(4)
print(original)   # [1, 2, 3, 4] - both point to the exact same list!

# 2. Shallow copy methods (creates a new, independent list)
copy_one = original.copy()
copy_two = original[:]
copy_three = list(original)

copy_one.append(99)
print(original)   # [1, 2, 3, 4] - unchanged
print(copy_one)   # [1, 2, 3, 4, 99]