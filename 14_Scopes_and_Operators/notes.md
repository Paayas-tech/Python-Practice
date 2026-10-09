# Section 14: Scopes and Operators

* **Variable Scopes (LEGB Rule):**
  * Python searches for names in: **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in.
  * The `global` keyword allows reassigning a module-level global variable from inside a function.

* **Operators:**
  * **Unary:** Acts on a single operand (e.g., `-x`, `not flag`).
  * **Binary:** Acts between two operands (e.g., `a + b`, `x == y`).

* **Truthy vs Falsy:**
  * Falsy values: `0`, `0.0`, `""`, `None`, `False`, `[]`, `{}`, `set()`, `()`.
  * Everything else evaluates to `True`.

* **Short-Circuit Evaluation:**
  * `a or b`: Evaluates `a`; if truthy, returns `a` immediately without checking `b`.
  * `a and b`: If `a` is falsy, returns `a` immediately; otherwise returns `b`.
* **The `del` Statement:** Deletes variable references from namespace or elements from mutable collections.