# 1. Generator Expression: (expression for item in iterable)
# Evaluates lazily on demand, preserving memory
gen_squares = (n ** 2 for n in range(5))
print("Generator object:", gen_squares)

# Iterating manually using next()
print(next(gen_squares))  # 0
print(next(gen_squares))  # 1

# Consuming the rest via loop
for val in gen_squares:
    print("Loop val:", val)  # 4, 9, 16


# 2. Generator Function using the 'yield' keyword
def countdown(start):
    while start > 0:
        yield start
        start -= 1


timer = countdown(3)
for step in timer:
    print(f"Step: {step}")