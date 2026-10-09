# 1. Merging dictionaries using the ** operator
default_settings = {"theme": "dark", "notifications": True, "volume": 50}
user_overrides = {"volume": 80, "language": "en"}

merged_settings = {**default_settings, **user_overrides}
print("Merged settings:", merged_settings)  # 'volume' is overwritten to 80

# 2. Creating shallow clones of dictionaries
original = {"a": 1, "b": 2}
clone = {**original, "c": 3}
print("Original:", original)
print("Clone:", clone)