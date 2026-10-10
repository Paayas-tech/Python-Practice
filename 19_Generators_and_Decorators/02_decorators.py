from functools import wraps


# 1. Logging / Execution Wrapper Decorator
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling: {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished: {func.__name__}")
        return result
    return wrapper


@log_execution
def process_data(records_count):
    return f"Processed {records_count} rows"


print(process_data(500))


# 2. Argument Validation & Permission Check Decorator
def validate_non_negative(func):
    @wraps(func)
    def wrapper(amount, *args, **kwargs):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return func(amount, *args, **kwargs)
    return wrapper


@validate_non_negative
def withdraw(amount):
    return f"Withdrawal of ${amount} approved."


print(withdraw(150))
# withdraw(-20)  # Raises ValueError