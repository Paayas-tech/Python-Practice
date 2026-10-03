import copy

# 1. Immutable objects (str, int, float, tuple) create new objects when altered
val = 10
original_id = id(val)
val += 1
print(id(val) == original_id)  # False: new object created

# 2. Mutable objects (list, dict, set) mutate in place
user_skills = ["SQL"]
user_skills.append("Python")
print(user_skills)  # ['SQL', 'Python']

# 3. Nested objects: Shallow copy vs Deep copy
nested_original = [["a", "b"], [1, 2]]

# Shallow copy shares references to nested collections
shallow = nested_original.copy()
# Deep copy creates completely independent copies of all nested layers
deep = copy.deepcopy(nested_original)

nested_original[0].append("c")
print("Shallow affected:", shallow)  # [['a', 'b', 'c'], [1, 2]]
print("Deep unaffected:", deep)      # [['a', 'b'], [1, 2]]