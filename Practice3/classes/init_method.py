# Here is a class using the __init__ constructor method
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

    # Here is the __str__ method to return a readable string representation
    def __str__(self):
        return f"{self.brand} laptop with {self.ram}GB RAM (${self.price})"

# Here is creating objects with individual values using the constructor
laptop1 = Laptop("Apple", 16, 1200)
laptop2 = Laptop("Dell", 32, 1400)

print(laptop1)
print(laptop2)