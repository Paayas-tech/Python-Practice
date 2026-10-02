nums = [10, 50, 20]

# Adding items
nums.append(30)            # Adds to end: [10, 50, 20, 30]
nums.insert(1, 15)         # Inserts at index 1: [10, 15, 50, 20, 30]
nums.extend([40, 60])      # Appends multiple elements

# Removing items
nums.pop()                 # Removes last item (60)
nums.pop(0)                # Removes item at index 0 (10)
nums.remove(50)            # Removes first occurrence of value 50

# Ordering
nums.sort()                # Sorts in-place (ascending)
nums.reverse()             # Reverses list in-place

print("Final list:", nums)