# Section 02: Formatting & PEP 8

* **Indentation:** Python uses 4 spaces per indent level after a colon `:` to define blocks (functions, `if` statements, loops). Omitting it causes `IndentationError`.
* **PEP 8 Spacing Rules:**
  * 2 blank lines before and after top-level functions or classes.
  * No whitespace right inside parentheses: `print("name")`, not `print( "name" )`.
  * Max line length recommendation: 79 characters.

  ## Comments in Python

* **Single-line:** Uses `#`. Python ignores everything after `#` on that line.
* **Inline Comments:** Placed on the same line after code; PEP 8 requires at least **2 spaces** before `#`.
* **Multi-line / Docstrings:** Uses triple quotes (`"""` or `'''`). Used for file/function documentation or multi-line notes.