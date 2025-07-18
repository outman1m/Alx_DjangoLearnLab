from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
=======

>>>>>>> ed228743dd938275dad90f9ce632d069667f25d8
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
<<<<<<< HEAD
=======

>>>>>>> ed228743dd938275dad90f9ce632d069667f25d8
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
<<<<<<< HEAD
=======

>>>>>>> ed228743dd938275dad90f9ce632d069667f25d8
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
<<<<<<< HEAD
=======

>>>>>>> ed228743dd938275dad90f9ce632d069667f25d8
    def __str__(self):
        return self.name
