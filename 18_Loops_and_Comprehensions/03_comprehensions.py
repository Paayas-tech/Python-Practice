raw_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. List Comprehension: [expression for item in iterable if condition]
squared_evens = [n ** 2 for n in raw_numbers if n % 2 == 0]
print("Squared evens:", squared_evens)  # [4, 16, 36, 64]

# 2. Set Comprehension: {expression for item in iterable}
unique_lengths = {len(word) for word in ["apple", "cat", "banana", "dog"]}
print("Unique word lengths:", unique_lengths)  # {3, 5, 6}

# 3. Dictionary Comprehension: {key_expr: val_expr for item in iterable}
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
student_scores = {name: score for name, score in zip(names, scores)}
print("Student scores dict:", student_scores)

# Transforming an existing dictionary
passed_students = {k: v for k, v in student_scores.items() if v >= 80}
print("Passed students:", passed_students)

# 4. Generator Expression / Tuple equivalent (returns generator, not tuple)
# Use tuple() constructor to materialize
gen_tuples = tuple(n * 10 for n in range(4))
print("Materialized tuple:", gen_tuples)  # (0, 10, 20, 30)

# 5. Chaining / Nested For-In expressions
matrix = [[1, 2], [3, 4]]
flattened = [val for row in matrix for val in row]
print("Flattened matrix:", flattened)  # [1, 2, 3, 4]