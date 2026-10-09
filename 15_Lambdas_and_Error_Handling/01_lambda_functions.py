# 1. Basic lambda syntax: lambda arguments: expression
square = lambda x: x ** 2
print("Square of 5:", square(5))


# 2. Returning lambda functions from factory functions
def create_multiplier(factor):
    return lambda n: n * factor


doubler = create_multiplier(2)
tripler = create_multiplier(3)
print("Doubled:", doubler(10))  # 20
print("Tripled:", tripler(10))  # 30


# 3. Sorting complex lists using a custom lambda key
users = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]
users.sort(key=lambda user: user["score"])
print("Sorted by score:", users)


# 4. Filtering sequences using filter() and lambda
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)