# Here is a function that calculates and returns a value
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

temperature_f = celsius_to_fahrenheit(25)
print(f"25°C is equal to {temperature_f}°F")


# Here is a function that returns a boolean value
def is_even_number(number):
    return number % 2 == 0

print(f"Is 10 even? {is_even_number(10)}")
print(f"Is 7 even? {is_even_number(7)}")


# Here is a function that returns multiple values as a tuple
def get_min_and_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lowest, highest = get_min_and_max([12, 45, 2, 89, 34])
print(f"Lowest: {lowest}, Highest: {highest}")