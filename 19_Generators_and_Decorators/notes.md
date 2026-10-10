# Section 19: Generators and Decorators

* **Generators:**
  * Created via generator expressions `(x for x in data)` or functions with `yield`.
  * **Lazy Evaluation:** Yields items one at a time via `next()` without loading the full collection into RAM.
  * Exhausted once iterated; cannot be rewound.

* **Decorator Functions (`@decorator`):**
  * Higher-order functions that take a target function as input, extend or wrap its behavior, and return the modified wrapper.
  * Must support `*args` and `**kwargs` inside the inner `wrapper` to handle any signature.
  * Use `@wraps(func)` from `functools` to preserve the original function's name and metadata.
  * Primary use cases: telemetry/logging, authentication/permission checks, caching, and input validation.