# Global variable
counter = 10


def update_local():
    # Local variable with same name (shadows global)
    counter = 5
    print("Inside local scope:", counter)


update_local()
print("Global counter unchanged:", counter)


# Modifying global variable inside a function using the 'global' keyword
def modify_global():
    global counter
    counter = 99


modify_global()
print("Global counter modified:", counter)