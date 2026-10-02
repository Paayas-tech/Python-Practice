# range(stop) -> starts at 0, step 1
r1 = range(5)
print(list(r1))  # [0, 1, 2, 3, 4]

# range(start, stop) -> stop is non-inclusive
r2 = range(10, 15)
print(list(r2))  # [10, 11, 12, 13, 14]

# range(start, stop, step)
even_nums = range(0, 10, 2)
print(list(even_nums))  # [0, 2, 4, 6, 8]

# Ranges are memory-efficient sequences (support indexing without generating lists)
r3 = range(100, 1000, 10)
print(r3[0])       # 100
print(r3.start)    # 100
print(r3.stop)     # 1000
print(r3.step)     # 10
print(500 in r3)   # True