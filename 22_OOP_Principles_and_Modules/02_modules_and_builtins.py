# 1. Built-in modules (math, random, sys, datetime)
import math
import random
from datetime import datetime

# 2. Importing from custom subfolder package
# Syntax: from <folder>.<module_name> import <function_or_class>
from helpers.math_utils import calculate_discount, format_currency

# Using built-ins
print("Pi constant:", round(math.pi, 4))
print("Random integer (1-100):", random.randint(1, 100))
print("Current timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Using custom imported functions
discounted = calculate_discount(150.0, 0.20)
print("Discounted total:", format_currency(discounted))