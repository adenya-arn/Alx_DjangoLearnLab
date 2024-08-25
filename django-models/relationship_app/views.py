import os
import django
import sys

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()





from relationship_app.models import Library, Author, Book, Librarian
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.generic import DetailView

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.http import HttpResponseForbidden
# Create your views here.

def home (request):
   return HttpResponse ("This is the home page")
   


def list_books(request, *args, **kwargs):
    books = Book.objects.all()  # Query all books
    return render(request, 'list_books.html', {'books': books})




class Library_Detail(DetailView):

    model = Library
    template_name = 'library_detail.html'

    context_object_name = 'library'
    
# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'

# Logout View
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'




User = get_user_model()

# Admin View
def admin_view(request):
    if request.user.is_authenticated and request.user.userprofile.role == 'Admin':
        return HttpResponse("Welcome Admin!")
    else:
        return HttpResponse("Access Denied: You are not an Admin.", status=403)

# Librarian View
def librarian_view(request):
    if request.user.is_authenticated and request.user.userprofile.role == 'Librarian':
        return HttpResponse("Welcome Librarian!")
    else:
        return HttpResponse("Access Denied: You are not a Librarian.", status=403)

# Member View
def member_view(request):
    if request.user.is_authenticated and request.user.userprofile.role == 'Member':
        return HttpResponse("Welcome Member!")
    else:
        return HttpResponse("Access Denied: You are not a Member.", status=403)



def add_book(request):
    if not request.user.has_perm('relationship_app.can_add_book'):
        return HttpResponseForbidden("You do not have permission to add a book.")
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Assuming you have a view to list books
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    if not request.user.has_perm('relationship_app.can_change_book'):
        return HttpResponseForbidden("You do not have permission to edit this book.")
    
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, book_id):
    if not request.user.has_perm('relationship_app.can_delete_book'):
        return HttpResponseForbidden("You do not have permission to delete this book.")
    
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})