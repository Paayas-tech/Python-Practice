# Section 05: Strings & String Formatting

* **Immutability:** Strings cannot be changed in place; methods return a new string.
* **Indexing & Slicing:** Zero-indexed; slicing syntax is `[start:stop:step]` where `stop` is exclusive.
* **Core Methods:** `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.split()`.
* **String Formatting:**
  * **f-strings** (`f"Hello {var}"`) are the modern standard: fast, clean, and supports inline expressions.
  * `.format()` and `%` are older alternative methods.