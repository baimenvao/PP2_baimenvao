# Here is custom sorting using lambda to sort strings by length
cities = ["Almaty", "Astana", "Shymkent", "Aktau"]
sorted_by_length = sorted(cities, key=lambda city: len(city))
print("Cities sorted by length:", sorted_by_length)


# Here is custom sorting using lambda to sort tuples by age
students = [("Amina", 20), ("Dias", 18), ("Dana", 22), ("Arman", 19)]
sorted_by_age = sorted(students, key=lambda student: student[1])
print("Students sorted by age:", sorted_by_age)


# Here is custom sorting using lambda to sort a list of dictionaries by price
products = [
    {"name": "Pen", "price": 1.5},
    {"name": "Notebook", "price": 4.0},
    {"name": "Backpack", "price": 25.0},
    {"name": "Eraser", "price": 0.8}
]
sorted_by_price = sorted(products, key=lambda item: item["price"], reverse=True)
print("Products sorted by price (descending):")
for product in sorted_by_price:
    print(f"  {product['name']}: ${product['price']}")
    