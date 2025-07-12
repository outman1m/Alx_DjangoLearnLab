from bookshelf.models import Book
book = Book.objects.first()
book.delete()
Book.objects.all()
# Output: (1, {'bookshelf.Book': 1})
# Output: <QuerySet []>
