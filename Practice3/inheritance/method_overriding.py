# Here is a base Animal class with a generic speak method
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

# Here is a Dog class overriding the speak method
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Here is a Cat class overriding the speak method
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Here is demonstrating method overriding with different child instances
dog = Dog("Rex")
cat = Cat("Milo")

print(dog.speak())
print(cat.speak())