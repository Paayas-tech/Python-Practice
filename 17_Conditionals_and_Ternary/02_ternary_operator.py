# Syntax: true_value if condition else false_value

# 1. Basic inline assignment
status_code = 200
status_msg = "Success" if status_code == 200 else "Error"
print("Status:", status_msg)

# 2. Discount calculation
purchase_total = 120
discount = 0.15 if purchase_total > 100 else 0.05
final_price = purchase_total * (1 - discount)
print(f"Final price: ${final_price:.2f}")

# 3. Data manipulation / Normalization
raw_data = None
clean_data = raw_data if raw_data is not None else "N/A"
print("Cleaned:", clean_data)

# 4. Multi-level ternary (use sparingly for readability)
score = 85
result = "Distinction" if score >= 90 else ("Pass" if score >= 60 else "Fail")
print("Grade tier:", result)