# 1. Type annotations for function parameters and return type
def validate_age(age: int) -> bool:
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age >= 18


# 2. Handling raised errors explicitly
try:
    print("Is adult:", validate_age(21))
    print("Is adult:", validate_age(-5))
except (TypeError, ValueError) as err:
    print("Validation failed:", err)