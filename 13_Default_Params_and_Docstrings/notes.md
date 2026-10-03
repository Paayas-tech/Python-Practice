# Section 13: Default Parameters and Docstrings

* **Default Parameters (`param=default`):**
  * Provide fallback values when arguments are omitted in the function call.
  * Must be defined **after** non-default parameters (`def fn(mandatory, optional=10):`).
  * **Mutable Default Trap:** Never use mutable defaults like `[]` or `{}` because they evaluate once at definition time and persist across calls. Use `default=None` and initialize inside the function.

* **Docstrings (`"""..."""`):**
  * Placed as the first statement immediately under the function header to describe purpose, parameters, and return types.
  * Formatted following PEP 257 conventions.
  * Can be programmatically inspected via `fn.__doc__` or the built-in `help(fn)` function.

  ## Callback Functions & Best Practices

* **First-Class Citizens:** In Python, functions can be assigned to variables, stored in data structures, and passed into other functions as arguments.
* **Callback Function:** A function passed as an argument to another function, intended to be called ("called back") within that outer function.
* **Reference vs Call:** Always pass the function reference (`callback_fn`), not the evaluated call (`callback_fn()`), when supplying callbacks.
* **Core Function Rules:**
  * Functions should perform a single, clear task.
  * Avoid unintended side effects on external mutable data.