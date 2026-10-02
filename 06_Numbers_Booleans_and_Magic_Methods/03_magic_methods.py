# Magic (dunder) methods are what Python calls under the hood

# Arithmetic operators invoke dunder methods
a = 10
b = 5
print(a + b)            # Normal addition
print(a.__add__(b))     # What happens behind the scenes

# String representation and length
text = "Analytics"
print(len(text))        # 9
print(text.__len__())   # Behind the scenes

# Equality check
print(a == b)           # False
print(a.__eq__(b))      # Behind the scenes