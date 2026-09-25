# Section 01: Functions & Built-in Functions

## Key Takeaways

1. **Calling Functions:**
   - Executed using parentheses `()`.
   - Arguments are passed inside the parentheses.

2. **Core Built-in Utilities:**
   - `print()`: Displays standard output to the console.
   - `type(obj)`: Returns the class/type of an object.
   - `id(obj)`: Returns the memory location identity number.
   - `len(seq)`: Returns the number of items in a sequence or collection.
   - `sum(seq)`: Computes the sum of numeric items in an iterable.
   - `min(seq)`, `max(seq)`: Finds extreme values.
   - `round(number[, ndigits])`: Rounds a numeric value to the nearest integer or specified decimal places.

3. **Type Casting Functions:**
   - `int()`, `float()`, `str()`, `bool()`, `list()`, `dict()` convert between types or construct new class instances.

4. **Functions vs. Methods:**
   - **Built-in Functions:** Called directly with arguments: `len(name)`, `print(val)`.
   - **Methods:** Tied to an object instance and accessed via dot notation: `name.upper()`.

5. **Return Values:**
   - A function without an explicit `return` statement implicitly returns `None` (type `NoneType`).

-----------------------------------------------------------------------
-----------------------------------------------------------------------

## Defining Custom Functions

### 1. Syntax & Indentation
- Defined using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.
- Python uses **4 spaces indentation** to define the code block inside the function body.
- Defining a function stores it in memory; it will not execute until called with parentheses `()`.

### 2. Parameters vs. Arguments
- **Parameters:** Variables listed in the function definition inside `def my_fn(param1, param2):`.
- **Arguments:** The actual values passed into the function when calling it: `my_fn(val1, val2)`.

### 3. Local Scope
- Parameters and variables initialized inside a function body are strictly **local**.
- Attempting to reference them outside the function raises a `NameError`.

### 4. Positional Argument Rules
- In standard definitions, all listed parameters are required.
- Omitting arguments or passing fewer than declared raises a `TypeError` (missing required positional argument).

> **Best Practice Tip:** Avoid using `sum` as a local variable name inside your functions. `sum` is a Python built-in function, and assigning a variable to it will temporarily overwrite ("shadow") the built-in function in that scope.

-----------------------------------------------------------------------
-----------------------------------------------------------------------

## The `return` Statement

### 1. Returning vs. Printing
- `print()` outputs data to the terminal console for human viewing; it does not pass data to subsequent code.
- `return` sends a value back to the caller so it can be assigned to a variable, piped into other calculations, or passed to other functions.

### 2. Function Termination & Unreachable Code
- As soon as Python encounters a `return` statement, the function immediately terminates execution.
- Any statements indented under the function directly after `return` become **unreachable** (flagged as warnings by linters in VS Code).

### 3. Implicit Return (`NoneType`)
- If a function does not contain an explicit `return` statement, Python automatically evaluates it to `None`.
- `None` represents the absence of a value and belongs to the built-in type `NoneType`.

-----------------------------------------------------------------------
-----------------------------------------------------------------------

## Exploring Built-in Functions & Signatures

### 1. Function References vs. Invocations
- `print`: References the built-in function object itself (`<built-in function print>`).
- `print()`: Executes/invokes the function.
- Because `print()` always returns `None`, wrapping it inside another call like `print(print("hi"))` evaluates the inner print first, then prints `None`.

### 2. Standard Streams (I/O)
- **`stdin` (Standard In):** Input channel receiving data (e.g., from `input()`).
- **`stdout` (Standard Out):** Output channel where terminal messages are displayed (e.g., from `print()`).
- **`stderr` (Standard Error):** Output channel used for error tracing and stack traces.

### 3. Key `print()` Keyword Arguments
- `sep`: Defines the delimiter between multiple comma-separated arguments (default is a single space `' '`).
- `end`: Specifies what is printed at the very end of the call (default is a newline character `'\n'`).
- Signature overview:
  `print(*values, sep=' ', end='\n', file=None, flush=False) -> None`

### 4. Reading Signatures & Documentation
- **Return Type Annotation:** The `->` notation in function definitions shows what type is returned (e.g., `dir() -> list[str]`, `input() -> str`, `print() -> None`).
- In VS Code, hover over any built-in or press **Ctrl + Hover** / **F1 (Quick Documentation)** to inspect its parameters and return types.

-----------------------------------------------------------------------
-----------------------------------------------------------------------

## Object & Scope Inspection with `dir()`

### 1. What `dir()` Does
- **`dir()` without arguments:** Returns a list of strings representing valid attributes and variable names in the local/global scope.
- **`dir(object)` with an argument:** Returns a list of all valid attributes and methods belonging to that specific object, module, or class.

### 2. Dunder (Double Underscore) Attributes
- Names starting and ending with two underscores (e.g., `__name__`, `__doc__`, `__builtins__`) are reserved by Python for internal system hooks and metadata.
- In the file being directly executed, `__name__` is always set to `"__main__"`.

### 3. The `__builtins__` Module
- Contains all predefined functions (`print`, `abs`, `min`), constructors (`int`, `str`, `list`), and standard error classes (`NameError`, `KeyError`, `ArithmeticError`).
- Can be inspected dynamically using `dir(__builtins__)`.

-----------------------------------------------------------------------
-----------------------------------------------------------------------

input("prompt"): Pauses execution to wait for user terminal input.

Always returns a string: Even if the user types numbers (e.g. "777"), the returned data type is always str. Methods like .upper() can be called directly on it.