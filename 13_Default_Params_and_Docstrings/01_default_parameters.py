# 1. Defining functions with default parameter values
def create_greeting(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(create_greeting("Paayas"))               # Uses default: "Hello, Paayas!"
print(create_greeting("Paayas", "Welcome"))    # Overrides default: "Welcome, Paayas!"


# 2. Positional order rule: default parameters MUST follow non-default parameters
def calculate_total(price, tax_rate=0.05, discount=0.0):
    return price * (1 - discount) * (1 + tax_rate)


print(round(calculate_total(100), 2))                # 105.0
print(round(calculate_total(100, discount=0.10), 2)) # 94.5


# 3. Pitfall: Avoid using mutable objects (like lists/dicts) as defaults
# Bad: def add_user(user, users_list=[]) -> shares state across calls!
# Good: Use None as default sentinel
def add_user_safely(user, users_list=None):
    if users_list is None:
        users_list = []
    users_list.append(user)
    return users_list


print(add_user_safely("Alice"))  # ['Alice']
print(add_user_safely("Bob"))    # ['Bob']