from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984 by George Orwell (1949)>
