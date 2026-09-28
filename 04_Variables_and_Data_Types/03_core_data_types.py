# Core data types overview
my_str = "Analytics"       # str
my_int = 42                # int
my_float = 3.14            # float
my_bool = True             # bool
my_list = [1, 2, 3]        # list (mutable sequence)
my_dict = {"name": "Bob"}  # dict (key-value pairs)

# Checking types using isinstance()
print(isinstance(my_str, str))         # True
print(isinstance(my_int, (int, float))) # True (matches either)
print(isinstance(my_list, dict))       # False