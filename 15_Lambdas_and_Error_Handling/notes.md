# Section 15: Lambda Functions & Error Handling

* **Lambda Functions:**
  * Anonymous, inline functions written as `lambda args: expression`.
  * Return value is computed implicitly (no `return` keyword allowed).
  * Ideal for short helper logic inside `sort(key=...)`, `filter()`, and `map()`.

* **Error Handling Blocks:**
  * `try`: Wraps code that might raise an exception.
  * `except ExceptionClass as err`: Catches and handles matching exceptions. Group multiple with `except (ErrA, ErrB):`.
  * `else`: Executes only if the `try` block succeeded with no exceptions.
  * `finally`: Always executes cleanup code whether an exception was raised or not.

* **Raising Exceptions & Typing:**
  * Use `raise ExceptionType("message")` to enforce data contracts and prevent silent bugs.
  * Parameter type hints (`def fn(x: int) -> bool:`) improve readability and static checking without changing runtime behavior.