set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: items in either set (set_a | set_b)
print("Union:", set_a.union(set_b))  # {1, 2, 3, 4, 5, 6}

# Intersection: items in both sets (set_a & set_b)
print("Intersection:", set_a.intersection(set_b))  # {3, 4}

# Difference: items in A but not in B (set_a - set_b)
print("Difference (A - B):", set_a.difference(set_b))  # {1, 2}

# Symmetric Difference: items in A or B, but not both (set_a ^ set_b)
print("Symmetric Difference:", set_a.symmetric_difference(set_b))  # {1, 2, 5, 6}