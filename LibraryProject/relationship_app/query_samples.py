<<<<<<< HEAD
from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

def get_books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

def get_librarian_for_library(library_name):
    return Librarian.objects.get(library__name=library_name)
=======
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
for book in library.books.all():
    print(book.title)

# 3. Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
print(librarian.name)
>>>>>>> ed228743dd938275dad90f9ce632d069667f25d8
