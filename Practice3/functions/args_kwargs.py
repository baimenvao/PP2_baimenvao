# Here is a function using *args to accept an arbitrary number of arguments
def calculate_total_expenses(*expenses):
    total = sum(expenses)
    print(f"Total expenses: ${total}")

calculate_total_expenses(50, 20, 15)
calculate_total_expenses(100, 250, 45, 12, 8)


# Here is a function using **kwargs to accept arbitrary keyword arguments
def display_user_profile(**user_info):
    print("User Profile Information:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")

display_user_profile(name="Alisher", age=20, city="Almaty", major="IT")


# Here is a function that combines positional arguments, *args, and **kwargs
def create_order(customer_name, *items, **delivery_details):
    print(f"\nOrder for: {customer_name}")
    print("Items ordered:", ", ".join(items))
    print(f"Deliver to: {delivery_details.get('address', 'Not specified')}")

create_order("Madina", "Laptop", "Mouse", address="Abay Ave 10", urgent=True)