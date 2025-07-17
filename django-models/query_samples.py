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
