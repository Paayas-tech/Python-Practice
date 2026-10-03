def multiply(a, b):
    """
    Multiply two numbers and return the calculated product.

    :param a: int or float
    :param b: int or float
    :return: Product of a and b
    """
    return a * b


# 1. Calling the function normally
result = multiply(4, 5)
print("Product:", result)

# 2. Inspecting the docstring via the __doc__ magic attribute
print("\n--- Docstring via __doc__ ---")
print(multiply.__doc__)

# 3. Inspecting the docstring using the built-in help() function
print("\n--- Help documentation ---")
help(multiply)