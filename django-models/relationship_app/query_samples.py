import os
import django
import sys

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian


#Query all books by a specific author.
#def books_by_author():

"""author_name = str(input("Name of author whose books you want:"))
authors = Author.objects.get(name = author_name )
books_by_author = Book.objects.filter(author = authors)

for book in books_by_author:
    print(book.title)
    #print(f"books by author/n {book_list} ")


#List all books in a library.
#def books_in_library():
library_name = str(input("Library name:"))
lib_id = Library.objects.get(name = library_name)
print(library_name)
books = lib_id.books.all()
book_list = []
for b in books:
    book_list.append(b.title)
    
print(book_list) 

    #print(books_by_libarary)
    
    
#Retrieve the librarian for a library.
#def library_librarian():
library_name = str(input("Name of library:"))
lib_id = Library.objects.get(name = library_name)

librarian_name = Librarian.objects.get(library = lib_id)
print(librarian_name)


#library_librarian()
#books_in_library()
#books_by_author()
"""



# Query all books by a specific author
author_name = str(input("Name of author whose books you want: "))
authors = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=authors)

for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = str(input("Library name: "))
lib_id = Library.objects.get(name=library_name)
books = lib_id.books.all()

book_list = []
for b in books:
    book_list.append(b.title)

print(book_list)

# Retrieve the librarian for a library
library_name = str(input("Name of library: "))
lib_id = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=lib_id)

print(librarian.name)



"""
# Query all books by a specific author
author_name = str(input("Name of author whose books you want: "))
try:
    authors = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=authors)
    
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(book.title)
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# List all books in a library
library_name = str(input("Library name: "))
try:
    lib_id = Library.objects.get(name=library_name)
    print(f"Books in {library_name}:")
    
    books = lib_id.books.all()  # Fetch books related to this library via ManyToManyField
    book_list = [book.title for book in books]
    
    if book_list:
        for book in book_list:
            print(book)
    else:
        print(f"No books found in {library_name}.")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")


# Retrieve the librarian for a library
library_name = str(input("Name of library: "))
try:
    lib_id = Library.objects.get(name=library_name)
    librarian_name = Librarian.objects.get(library=lib_id)
    print(f"The librarian of {library_name} is {librarian_name.name}.")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}.")

"""

