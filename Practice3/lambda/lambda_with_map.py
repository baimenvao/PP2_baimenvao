# Here is a map function using lambda to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)


# Here is a map function using lambda to convert Celsius to Fahrenheit
celsius_temperatures = [0, 15, 25, 30]
fahrenheit_temperatures = list(map(lambda c: (c * 9 / 5) + 32, celsius_temperatures))
print("Fahrenheit temperatures:", fahrenheit_temperatures)


# Here is a map function using lambda to format names with capital letters
names = ["ayazhan", "arman", "dana"]
formatted_names = list(map(lambda name: name.capitalize(), names))
print("Formatted names:", formatted_names)