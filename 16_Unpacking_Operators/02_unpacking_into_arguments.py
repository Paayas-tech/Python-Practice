def calculate_box_volume(length, width, height):
    return length * width * height


# 1. Unpacking a list/tuple into positional parameters with *
dimensions = [10, 5, 2]
volume = calculate_box_volume(*dimensions)
print("Volume from list unpacking:", volume)


# 2. Unpacking a dictionary into keyword arguments with **
box_dict = {"length": 8, "width": 4, "height": 3}
volume_from_dict = calculate_box_volume(**box_dict)
print("Volume from dict unpacking:", volume_from_dict)