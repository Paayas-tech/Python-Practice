profile = {"user": "Paayas", "city": "Delhi"}

# 1. Safe access using .get() (avoids KeyError if key doesn't exist)
print(profile.get("city"))                   # 'Delhi'
print(profile.get("country"))                # None
print(profile.get("country", "Not Found"))  # Default fallback: 'Not Found'

# 2. Extracting keys, values, and pairs
print(list(profile.keys()))    # ['user', 'city']
print(list(profile.values()))  # ['Paayas', 'Delhi']
print(list(profile.items()))   # [('user', 'Paayas'), ('city', 'Delhi')]

# 3. Merging / Updating dictionaries
profile.update({"role": "Analyst", "active": True})
print(profile)

# 4. Removing items safely
removed_val = profile.pop("active")
print("Removed:", removed_val)