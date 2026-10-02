raw_text = "   Data Analysis with Python   "

# Cleaning whitespace
cleaned = raw_text.strip()
print(cleaned)

# Case conversions
print(cleaned.lower())
print(cleaned.upper())
print(cleaned.title())

# Searching and replacing
print(cleaned.replace("Python", "SQL"))
print(cleaned.count("a"))
print(cleaned.startswith("Data"))

# Splitting into a list
words = cleaned.split(" ")
print(words)