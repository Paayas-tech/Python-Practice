# Section 10: Sequences & Object Mutation

* **Sequence Built-ins:** `len()`, `min()`, `max()`, and `sum()` work uniformly across sequential data types (`list`, `tuple`, `str`, `range`).
* **`zip(*iterables)`:** Aggregates elements from each iterable into tuples. Calling `dict(zip(keys, values))` is a fast pattern for building dictionaries from paired lists.
* **Mutability:**
  * **Immutable:** `int`, `float`, `str`, `tuple`, `bool`. Operations that change them always create a new object in memory.
  * **Mutable:** `list`, `dict`, `set`. Operations can modify their contents in place at the same memory address.
* **Shallow vs. Deep Copy:**
  * `shallow = original.copy()` copies only the top-level container; inner nested lists or dicts remain referenced.
  * `copy.deepcopy()` recursively duplicates all nested objects, preventing side effects during mutations.