# Here is a basic lambda function that adds 10 to a number
add_ten = lambda number: number + 10
print("Result of adding 10 to 5:", add_ten(5))


# Here is a lambda function with multiple arguments to calculate rectangle area
calculate_area = lambda width, height: width * height
print("Area of rectangle (4x6):", calculate_area(4, 6))


# Here is a function that returns an anonymous lambda function
def make_multiplier(factor):
    return lambda value: value * factor

triple = make_multiplier(3)
print("Triple of 7 is:", triple(7))