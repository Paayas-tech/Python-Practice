# *args gathers arbitrary positional arguments into a tuple
def sum_numbers(*args):
    print("Type of args:", type(args))  # <class 'tuple'>
    print("Arguments passed:", args)
    return sum(args)


print(sum_numbers(10, 20))           # 30
print(sum_numbers(5, 15, 25, 35))     # 80
print(sum_numbers())                 # 0