#first we import
from bookshelf import Book

#How to create an instance
Book = Book.objects.create(title = "1984", author = "George Orwell", publication_year = "1949")

#Save what we have just done
book.save()
