# 1. Handling multiple specific exceptions
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as error:
        print(f"Error caught: {error}")
    except TypeError as error:
        print(f"Type mismatch: {error}")
    else:
        # Runs only if NO exception occurred in try
        print("Division successful, result:", result)
    finally:
        # Always runs, regardless of success or errors
        print("Execution of divide() complete.")


divide(10, 2)
divide(10, 0)
divide(10, "5")

# 2. Catching multiple error classes in a single except tuple
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except (FileNotFoundError, IOError) as error:
    print(f"File handling issue: {error}")