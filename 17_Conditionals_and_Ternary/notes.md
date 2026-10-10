# Section 17: Conditional Statements and Ternary Operator

* **`if-elif-else` Rules:**
  * Evaluated from top to bottom; execution halts at the first matching truthy branch.
  * Always arrange boundary conditions in logical sequence (e.g., descending thresholds for scores).
  * Use **guard clauses** (early `return`) inside functions to avoid deeply nested blocks.

* **Ternary Operator (Conditional Expression):**
  * **Syntax:** `value_if_true if condition else value_if_false`.
  * Returns an evaluated expression directly, making it suitable for inline assignments and function arguments.
  * Avoid nesting multiple ternary expressions when a standard `if-elif-else` block provides clearer readability.