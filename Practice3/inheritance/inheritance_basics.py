# Here is a parent class representing a general Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

# Here is a child class Car inheriting directly from the Vehicle class
class Car(Vehicle):
    pass

# Here is creating a child class object and using inherited methods
my_car = Car("Toyota", "Camry")
my_car.display_info()