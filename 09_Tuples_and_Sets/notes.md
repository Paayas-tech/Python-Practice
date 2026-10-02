# Section 09: Tuples and Sets

* **Tuples `( )`:**
  * Ordered, indexed, and **immutable** (cannot add, delete, or modify items).
  * Used for fixed data integrity and unpacking (`a, b = (1, 2)`).
  * Common methods: `.count()`, `.index()`.

* **Sets `{ }`:**
  * Unordered, unindexed collections of **unique** elements.
  * Rapid membership testing (`x in my_set`) and removing list duplicates: `list(set(items))`.

* **Set Theory Operations:**
  * **Union (`|` or `.union()`):** All elements from both sets.
  * **Intersection (`&` or `.intersection()`):** Elements common to both.
  * **Difference (`-` or `.difference()`):** Elements in the first set but not the second.
  * **Symmetric Difference (`^` or `.symmetric_difference()`):** Elements in either set, excluding common ones.

  ## Ranges in Python

* **Syntax:** `range(start, stop, step)` where `start` defaults to `0`, `step` defaults to `1`, and `stop` is exclusive.
* **Lazy Evaluation:** Generates numbers on demand rather than storing them in memory, making large ranges (like `range(1_000_000)`) highly efficient.
* **Conversion:** Convert to a list using `list(range(...))` or tuple using `tuple(range(...))`.
* **Attributes:** `.start`, `.stop`, `.step`.