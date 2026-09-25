# 1. Gathering string input
my_name = input("Please enter your name: ")
print(my_name)

# 2. Gathering input and checking type (always str)
my_favorite_num = input("Please enter your favorite number: ")
print(my_favorite_num)
print(type(my_favorite_num))  # Always <class 'str'>

# 3. Using a string method on user input
print(my_name.upper())