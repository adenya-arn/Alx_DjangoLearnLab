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
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import Book, Author
from django.http import HttpResponseForbidden


# Create your views here.

def home (request):
   return HttpResponse ("This is the home page")
   


def list_books(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view this page.")
    
    books = Book.objects.all()
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
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        
        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                Book.objects.create(title=title, author=author)
                return redirect('book_list')  # Redirect to the book list or another page
            except Author.DoesNotExist:
                return HttpResponse("Author not found.")
        else:
            return HttpResponse("Missing title or author ID.")
    
    return render(request, 'add_book.html')

def edit_book(request, book_id):
    if not request.user.has_perm('relationship_app.can_change_book'):
        return HttpResponseForbidden("You do not have permission to edit this book.")
    
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        
        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                book.title = title
                book.author = author
                book.save()
                return redirect('book_list')  # Redirect to the book list or another page
            except Author.DoesNotExist:
                return HttpResponse("Author not found.")
        else:
            return HttpResponse("Missing title or author ID.")
    
    return render(request, 'edit_book.html', {'book': book})

def list_books(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to view this page.")

    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})


# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            return HttpResponse("Invalid login credentials.")

    return render(request, 'login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Registration view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

# View for adding a book (permission check without decorator)
def add_book(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to add books.")

    if not request.user.has_perm('relationship_app.can_add_book'):
        return HttpResponseForbidden("You do not have permission to add books.")

    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        Book.objects.create(title=title, author_id=author_id)
        return redirect('book_list')

    return render(request, 'add_book.html')

# View for editing a book (permission check without decorator)
def edit_book(request, book_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to edit books.")

    if not request.user.has_perm('relationship_app.can_change_book'):
        return HttpResponseForbidden("You do not have permission to edit books.")

    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author_id = author_id
        book.save()
        return redirect('book_list')

    return render(request, 'edit_book.html', {'book': book})

# View for deleting a book (permission check without decorator)
def delete_book(request, book_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to delete books.")

    if not request.user.has_perm('relationship_app.can_delete_book'):
        return HttpResponseForbidden("You do not have permission to delete books.")

    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'delete_book.html', {'book': book})

# Admin view example
def admin_view(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to access this page.")

    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to access this page.")

    # Render your admin page content here
    return HttpResponse("Admin View")
