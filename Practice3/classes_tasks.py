import math

# ==========================================
# Task 1: Class with getString and printString
# ==========================================
# Here is a class to get and print string in uppercase
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())


# ==========================================
# Task 2: Shape and Square classes
# ==========================================
# Here is a Shape class and its subclass Square
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


# ==========================================
# Task 3: Rectangle inheriting from Shape
# ==========================================
# Here is a Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# ==========================================
# Task 4: Point class
# ==========================================
# Here is a Point class with show, move, and dist methods
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)


# ==========================================
# Task 5: Bank Account class
# ==========================================
# Here is a Bank Account class with deposits and withdrawals
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} accepted. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted. Remaining balance: ${self.balance}")
        else:
            print(f"Withdrawal of ${amount} declined. Funds unavailable! (Balance: ${self.balance})")


# ==========================================
# Task 6: Filter prime numbers using filter and lambda
# ==========================================
# Here is a program to filter prime numbers from a list using lambda and filter
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20, 23]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))


# ==========================================
# Testing the solutions
# ==========================================
if __name__ == "__main__":
    print("--- Task 2 & 3: Shape, Square, Rectangle ---")
    shape = Shape()
    print("Default Shape Area:", shape.area())
    square = Square(5)
    print("Square Area (side 5):", square.area())
    rect = Rectangle(4, 6)
    print("Rectangle Area (4x6):", rect.area())

    print("\n--- Task 4: Point ---")
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    p1.show()
    p2.show()
    print(f"Distance between p1 and p2: {p1.dist(p2)}")
    p1.move(0, 0)
    p1.show()

    print("\n--- Task 5: Account ---")
    acc = Account("Amina", 100)
    acc.deposit(50)
    acc.withdraw(100)
    acc.withdraw(80)  # Should decline

    print("\n--- Task 6: Filter Prime Numbers ---")
    print("Original numbers:", numbers)
    print("Prime numbers:", prime_numbers)