from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """الحصول على جميع كتب مؤلف معين"""
    return Book.objects.filter(author__name=author_name)

def get_books_in_library(library_name):
    """الحصول على جميع الكتب في مكتبة معينة"""
    return Library.objects.get(name=library_name).books.all()

def get_librarian_for_library(library_name):
    """الحصول على أمين المكتبة لمكتبة معينة"""
    return Librarian.objects.get(library__name=library_name)

def create_sample_data():
    """إنشاء بيانات نموذجية للاختبار"""
    author = Author.objects.create(name="أحمد محمد")
    book1 = Book.objects.create(title="الكتاب الأول", author=author)
    book2 = Book.objects.create(title="الكتاب الثاني", author=author)
    library = Library.objects.create(name="المكتبة المركزية")
    library.books.add(book1, book2)
    librarian = Librarian.objects.create(name="علي حسين", library=library)
    return {
        'author': author,
        'books': [book1, book2],
        'library': library,
        'librarian': librarian
    }
