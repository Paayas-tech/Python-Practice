# Section 07: Lists in Python

* **Properties:** Ordered, mutable, indexed, and allows heterogeneous data types.
* **Mutation vs Immutability:** Unlike strings, list elements can be modified in-place without creating a new object (`list[0] = new_val`).
* **Essential Methods:**
  * Adding: `.append(x)`, `.insert(i, x)`, `.extend(iterable)`
  * Removing: `.pop([i])`, `.remove(val)`, `.clear()`
  * Ordering: `.sort()` (in-place), `sorted(list)` (returns new list), `.reverse()`
* **Copying Warning:** `b = a` assigns a memory pointer; altering `b` mutates `a`. Always use `a.copy()`, `a[:]`, or `list(a)` to create independent copies.