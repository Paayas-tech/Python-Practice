# Section 08: Dictionaries in Python

* **Structure:** Key-value pairs enclosed in curly braces `{key: value}`. Keys must be immutable and unique.
* **Accessing:**
  * `dict["key"]`: Raises `KeyError` if key is missing.
  * `dict.get("key", default)`: Safely returns `None` or the custom default value without raising an error.
* **Core Methods:**
  * `.keys()`: Returns all keys.
  * `.values()`: Returns all values.
  * `.items()`: Returns key-value pairs as tuples (essential for loops).
  * `.update(other_dict)`: Merges another dict into the current one.
  * `.pop(key)`: Removes key and returns its value.