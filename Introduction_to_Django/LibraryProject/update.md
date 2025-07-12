from bookshelf.models import Book
b = Book.objects.first()
b.title = "Nineteen Eighty-Four"
b.save()
b
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
