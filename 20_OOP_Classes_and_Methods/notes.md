# Section 20: Object-Oriented Programming (Classes & Methods)

* **Classes & Instances:**
  * A class serves as the blueprint; instances are concrete objects created from that blueprint.
  * `__init__(self, ...)` is the dunder constructor method executed automatically when an object is instantiated.
  * `self` represents the specific object instance being referenced or mutated.

* **Attributes:**
  * **Instance Attributes:** Assigned via `self.attribute = value` inside `__init__`. Unique to every instance.
  * **Class Attributes:** Defined directly in the class body. Shared across all instances of that class.

* **Method Types:**
  * **Instance Methods (`def method(self):`):** Operate on the specific instance state.
  * **Class Methods (`@classmethod`, `def method(cls):`):** Receive the class reference `cls` instead of `self`. Often used for factory constructors or class-wide state tracking.
  * **Static Methods (`@staticmethod`, `def method():`):** Plain utility functions attached to the class namespace without access to `self` or `cls`.

  ## Magic Methods (Dunder Methods)

* Special methods wrapped with double underscores that integrate classes with Python built-ins and operators.
* `__str__(self)`: Returns user-friendly text for `print()` and `str()`.
* `__repr__(self)`: Returns detailed debugging output for developers; should ideally look like valid Python code to recreate the object.
* `__len__(self)`: Allows calling `len(instance)`.
* `__eq__(self, other)`: Implements behavior for `==` comparisons.
* `__add__(self, other)`: Implements behavior for the `+` arithmetic operator.