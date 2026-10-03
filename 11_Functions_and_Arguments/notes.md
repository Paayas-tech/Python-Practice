# Section 11: Functions & Function Arguments

* **Shortest Function:** Defined with `def fn(): pass`, which returns `None` by default.
* **Parameters vs. Arguments:**
  * **Parameters:** Variable names declared inside the function definition header.
  * **Arguments:** Concrete values or references passed into the function when called.
* **Argument Mutability Behavior:**
  * **Immutable arguments (`int`, `str`, `tuple`):** Rebinding inside the function does not change external variables.
  * **Mutable arguments (`list`, `dict`, `set`):** In-place mutations (`.append()`, `.pop()`) directly affect the original caller's data.
* **Default Arguments:** Always specify optional parameters with defaults (`param=value`) *after* mandatory positional arguments.