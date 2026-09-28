# 1. Dynamic typing: a variable can change its type at runtime
var = 100
print(type(var))  # <class 'int'>

var = "Now a string"
print(type(var))  # <class 'str'>

# 2. Variables and memory references using id()
a = 10
b = a
print(id(a) == id(b))  # True: both point to the same memory object