# Proper parameter ordering: positional, *args, **kwargs
def process_order(item, *modifiers, **details):
    print(f"Item: {item}")
    print(f"Modifiers: {modifiers}")
    print(f"Details: {details}")


process_order(
    "Coffee", 
    "Extra Milk", "No Sugar", 
    size="Large", takeaway=True
)