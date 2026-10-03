# 1. The shortest possible function in Python uses the pass statement
def do_nothing():
    pass

print(do_nothing())  # Returns None


# 2. Parameters (placeholders in def) vs Arguments (actual values passed)
def greet_user(first_name, last_name):  # Parameters: first_name, last_name
    return f"Hello, {first_name} {last_name}!"

# Positional arguments: matched strictly by order
message = greet_user("Paayas", "Shrivastava")  # Arguments: "Paayas", "Shrivastava"
print(message)