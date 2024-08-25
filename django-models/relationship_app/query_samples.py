import os
import django
import sys

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian


"""
def create_author():
    Instance = str(input("Add authors name:"))
    add = Author.objects.create(name = Instance)
    create_Book(add)


def create_Book(author):
    Book.objects.create(title = str(input("Title of book is:")), author = author) 
    create_library()


def create_library():
    Name = str(input("Name of library;"))
   # book_name = str(input("Name of Book to add:"))
    Library.objects.create(name = Name) #ADA'books = book_name'
    create_librarian()

def create_librarian():
    Name = str(input("Librarian's name is:"))
    library = str(input("Working in which library:"))
    Librarian.objects.create(name = Name, library = library)  

create_author()"""




#Query all books by a specific author.
def books_by_author():

    author_name = str(input("Name of author whose books you want:"))
    authors = Author.objects.get(name = author_name )
    books_by_author = Book.objects.filter(author = authors)

    for book in books_by_author:
        print(book.title)
    #print(f"books by author/n {book_list} ")


#List all books in a library.
def books_in_library():
    lib_name = str(input("Library name:"))
    lib_id = Library.objects.get(name = lib_name)
    print(lib_name)
    books = lib_id.books.all()
    book_list = []
    for b in books:
        book_list.append(b.title)
    
    print(book_list) 

    #print(books_by_libarary)
    
    
#Retrieve the librarian for a library.
def library_librarian():
    library_name = str(input("Name of library:"))
    lib_id = Library.objects.get(name = library_name)

    librarian_name = Librarian.objects.get(library = lib_id)
    print(librarian_name)


library_librarian()
books_in_library()
books_by_author()

