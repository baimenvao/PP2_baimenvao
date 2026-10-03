# Here is a basic class definition for a Book
class Book:
    title = "Python Crash Course"
    author = "Eric Matthes"

# Here is creating an object from the Book class and reading its attributes
my_book = Book()
print(f"Book Title: {my_book.title}")
print(f"Author: {my_book.author}")


# Here is an empty class definition using the pass statement
class DraftNote:
    pass

# Here is creating an instance of the empty class
note = DraftNote()
print("DraftNote object created successfully:", note)