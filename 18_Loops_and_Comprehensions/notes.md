# Section 18: Loops and Comprehensions

* **`for-in` Loops:**
  * Used for definite iteration across any iterable (`list`, `tuple`, `str`, `dict`, `set`, `range`).
  * Dictionary iteration: use `.items()` to access both keys and values simultaneously.

* **`while` Loops & Control Statements:**
  * Executes indefinitely as long as its condition remains truthy.
  * `break`: Immediately exits the nearest enclosing loop.
  * `continue`: Skips the rest of the current iteration and advances to the next cycle.

* **Comprehensions:**
  * **List:** `[expr for item in iterable if condition]`
  * **Set:** `{expr for item in iterable if condition}`
  * **Dict:** `{k_expr: v_expr for item in iterable if condition}`
  * **Tuples:** `(expr for ...)` creates a lazy **generator expression**, which must be passed to `tuple()` to evaluate completely.
  * Comprehensions are more concise, readable, and often faster in CPython than standard `for` loops appending to an empty list.