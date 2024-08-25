import os
import django
import sys

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()





from relationship_app.models import Library, Author, Book, Librarian

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import DetailView
#from .models import Book
# Create your views here.

def home (request):
   return HttpResponse ("This is the home page")
   


def books_in_library_view(request, *args, **kwargs):
    #lib_name = str(input("Library name:"))
    #lib_id = Library.objects.get(name = lib_name)
    lib_id = Library.objects.get(id = 1)

    list = lib_id.books.all()
    book = {
        "books":list
    }
    #print(books)


    return render (request, 'list_books.html', book)
    #print(books)

#lists_all()




class Library_Detail(DetailView):

    #model = Book
    template_name = 'library_detail.html'
    book = Book.objects.all()

    book_list = {
        "library.book.all":book
    }
    
    return render (request, "library_detail.html", book_list)


