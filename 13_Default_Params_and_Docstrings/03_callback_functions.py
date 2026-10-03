# 1. Functions are first-class citizens: they can be passed as arguments
def print_number_info(num):
    if (num % 2) == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


# 2. Callback function: a function passed into another function to be executed
def process_user_input(callback_fn):
    num_str = input("Enter a number: ")
    num = int(num_str)
    # Execute the passed callback
    callback_fn(num)


# Pass the function reference (without parentheses) as an argument
process_user_input(print_number_info)