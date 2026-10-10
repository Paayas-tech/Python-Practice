# 1. if-elif-else ladder with condition order awareness
def calculate_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    
    # Check highest/strictest threshold first
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print("Score 95:", calculate_grade(95))
print("Score 73:", calculate_grade(73))
print("Score 52:", calculate_grade(52))


# 2. Guard clause / Return early pattern (cleaner than nested blocks)
def process_transaction(amount, is_verified):
    if amount <= 0:
        return "Amount must be positive"
    if not is_verified:
        return "Account verification required"
    
    return f"Processed payment of ${amount}"


print(process_transaction(-5, True))
print(process_transaction(100, False))
print(process_transaction(250, True))