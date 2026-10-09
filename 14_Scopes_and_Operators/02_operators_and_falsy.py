# 1. Unary vs Binary operators
x = 10
unary_neg = -x          # Unary operator (-)
unary_not = not True    # Unary logical operator (not)
binary_add = x + 5      # Binary operator (+)

print(unary_neg, unary_not, binary_add)

# 2. Falsy values evaluate to False in boolean context
# Falsy: 0, 0.0, "", None, [], {}, set(), False
falsy_values = [0, 0.0, "", None, [], {}, set(), False]
print("All are falsy:", all(not bool(val) for val in falsy_values))

# 3. Truthy values: Any non-zero number or non-empty sequence
val = "data"
if val:
    print(f"'{val}' is truthy")