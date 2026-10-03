# **kwargs gathers arbitrary keyword arguments into a dictionary
def print_user_info(**kwargs):
    print("Type of kwargs:", type(kwargs))  # <class 'dict'>
    print("Data received:", kwargs)


# Calling with arbitrary keyword arguments
print_user_info(name="Paayas", role="Data Analyst", city="Delhi")


# Merging keyword arguments into a dictionary
def merge_data(**kwargs):
    user_data = {"status": "active"}
    user_data.update(kwargs)
    return user_data


print(merge_data(id=101, plan="premium"))