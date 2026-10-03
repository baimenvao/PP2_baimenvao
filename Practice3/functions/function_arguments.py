# Here is a function with positional arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")

describe_pet("cat", "Puma")


# Here is a function with a default parameter value
def enroll_student(student_name, course="Computer Science"):
    print(f"Student {student_name} is enrolled in {course}.")

enroll_student("Ayau")  # Uses the default course
enroll_student("Biba", "Mathematics")  # Overrides the default course


# Here is a function that accepts a list as an argument
def print_shopping_list(items):
    print("Shopping List:")
    for item in items:
        print(f"- {item}")

groceries = ["Apples", "Milk", "Bread", "Eggs"]
print_shopping_list(groceries)
