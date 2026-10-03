# 1. Passing immutable objects (int, str, tuple): cannot be modified outside
def update_number(num):
    num += 10
    return num

count = 5
update_number(count)
print("Original count unaffected:", count)  # Still 5


# 2. Passing mutable objects (list, dict, set): modifications affect the original
def add_item(target_list, item):
    target_list.append(item)

my_items = ["apple", "banana"]
add_item(my_items, "cherry")
print("Original list mutated:", my_items)  # ['apple', 'banana', 'cherry']


# 3. Positional vs Keyword & Default (Optional) Arguments
def calculate_price(base_price, discount=0.0, tax=0.05):
    final_price = base_price * (1 - discount) * (1 + tax)
    return round(final_price, 2)

# Using defaults
print(calculate_price(100))                     # discount=0.0, tax=0.05 -> 105.0

# Overriding with keyword arguments
print(calculate_price(100, tax=0.10, discount=0.20))  # 88.0