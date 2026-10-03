import math

# Task 1
degree = float(input("Input degree: "))
print("Output radian:", math.radians(degree))

# Task 2
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
print("Expected Output:", 0.5 * (a + b) * h)

# Task 3
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area))

# Task 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
print("Expected Output:", float(base * height))