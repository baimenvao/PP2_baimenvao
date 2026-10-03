# Here is a parent class Employee with basic details
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

# Here is a child class Manager extending Employee using super()
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Here is calling the parent constructor with super()
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        # Here is extending the parent method using super()
        parent_details = super().get_details()
        return f"{parent_details}, Department: {self.department}"

# Here is testing the child class Manager
manager = Manager("Aigerim", 5000, "Engineering")
print(manager.get_details())