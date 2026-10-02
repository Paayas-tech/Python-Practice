# String basics, indexing, and slicing
text = "Python Analytics"

# Indexing (0-indexed, negative indexing from end)
print(text[0])   # 'P'
print(text[-1])  # 's'

# Slicing: [start:stop:step] (stop is non-inclusive)
print(text[0:6])   # 'Python'
print(text[7:])    # 'Analytics'
print(text[::-1])  # Reverses string

# Strings are immutable (cannot reassign text[0] = 'J')
print(len(text))