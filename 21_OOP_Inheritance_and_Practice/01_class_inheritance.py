# 1. Base (Parent) Class
class Vehicle:
    def __init__(self, brand: str, max_speed: int):
        self.brand = brand
        self.max_speed = max_speed

    def move(self):
        print(f"{self.brand} is moving at speed up to {self.max_speed} km/h")


# 2. Derived (Child) Class extending Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand: str, max_speed: int, battery_kwh: int):
        # Call the parent class __init__ method using super()
        super().__init__(brand, max_speed)
        self.battery_kwh = battery_kwh

    # Method Overriding: customizing parent behavior
    def move(self):
        super().move()
        print(f"Running silently on a {self.battery_kwh} kWh battery pack.")


# Creating an instance of the extended class
ev = ElectricCar("Tesla", 250, 75)
ev.move()
print(f"Is ev an instance of Vehicle? {isinstance(ev, Vehicle)}")
print(f"Is ElectricCar a subclass of Vehicle? {issubclass(ElectricCar, Vehicle)}")