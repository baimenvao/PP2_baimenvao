# Here is a class demonstrating class variables versus instance variables
class Student:
    # Class variable (shared by all students)
    university = "KBTU"

    def __init__(self, name, student_id):
        # Instance variables (unique to each individual student)
        self.name = name
        self.student_id = student_id

# Here is creating instances that share the same class variable
student1 = Student("Dias", "22B0101")
student2 = Student("Dana", "22B0202")

print(f"{student1.name} studies at {student1.university}")
print(f"{student2.name} studies at {student2.university}")

# Here is modifying an attribute of an object
student1.name = "Dias Serikov"
print(f"Updated name for student 1: {student1.name}")

# Here is deleting an attribute from an object using the del keyword
del student2.student_id
print("Deleted student_id property for student 2.")