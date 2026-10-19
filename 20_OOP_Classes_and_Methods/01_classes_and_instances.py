# 1. Basic Class definition and instantiating objects
class Car:
    pass

car_one = Car()
car_two = Car()
print("Instance one:", car_one)
print("Instance two:", car_two)

# 2. Adding attributes dynamically via dot notation
car_one.brand = "Toyota"
car_one.model = "Corolla"
print(f"Car 1: {car_one.brand} {car_one.model}")

# 3. Proper initialization using the __init__ constructor method
class Vehicle:
    def __init__(self, brand, model, year):
        # Instance attributes bound to the specific object
        self.brand = brand
        self.model = model
        self.year = year

vehicle_a = Vehicle("Honda", "Civic", 2022)
vehicle_b = Vehicle("Hyundai", "i20", 2024)

print(f"Vehicle A: {vehicle_a.brand} ({vehicle_a.year})")
print(f"Vehicle B: {vehicle_b.brand} ({vehicle_b.year})")