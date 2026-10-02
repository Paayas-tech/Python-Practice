# Section 06: Numeric Types, Booleans & Magic Methods

* **Numeric Types:**
  * `int`: Whole numbers; supports underscores for readability (`1_000_000`).
  * `float`: Decimals and scientific notation (`2.5e3`).
  * `complex`: Real and imaginary numbers (`3 + 5j`).
* **Booleans & Falsy Values:**
  * `bool` represents `True` or `False`.
  * Falsy values evaluate to `False` in conditions: `0`, `0.0`, `""`, `None`, empty collections (`[]`, `{}`). Everything else is Truthy.
* **Magic (Dunder) Methods:**
  * Internal methods with double underscores (e.g., `__add__`, `__len__`, `__eq__`).
  * Standard operations like `+`, `==`, and `len()` map directly to these methods under the hood.