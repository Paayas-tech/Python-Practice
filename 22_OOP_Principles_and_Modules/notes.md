# Section 22: OOP Core Principles, Modules & Execution Context

* **Four Pillars of OOP:**
  * **Encapsulation:** Grouping data and methods into objects while restricting direct external access (`_protected`, `__private`).
  * **Inheritance:** Enabling child classes to inherit attributes and methods from base classes (`class Child(Parent):`).
  * **Polymorphism:** Allowing different subclasses to implement methods of the same name with different internal logic.
  * **Abstraction:** Hiding complex low-level implementation details behind clean, enforced interfaces (`abc.ABC`, `@abstractmethod`).

* **Modules and Packages:**
  * **Module:** Any `.py` file containing functions, classes, or runnable code.
  * **Import syntax:**
    * `import module_name`: Imports full namespace.
    * `from module_name import item`: Imports specific functions or classes.
    * `from subfolder.module_name import item`: Imports from packages/subdirectories.
  * **Built-in modules:** Standard library utilities (`math`, `random`, `sys`, `datetime`, `pathlib`).

* **`if __name__ == "__main__":` Idiom:**
  * When run directly: Python sets `__name__ = "__main__"`.
  * When imported: Python sets `__name__ = "<module_name>"`.
  * Protects executable test code, CLI logic, or script operations from running automatically upon import.