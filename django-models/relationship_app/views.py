from django.shortcuts import render, redirect, HttpResponse
from .models import Library, Book
from django.views.generic import DetailView
from .forms import LibraryName, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def home(request, *args, **kwargs):
    return HttpResponse ("Welcome to the home page")


def list_books (request, *args, **kwargs):

    books = Book.objects.all()
    context = {
        'books': books
    }

    return render (request, 'relationship_app/list_books.html', context)
    

class LibraryDetailView(DetailView):

    model = Library
    template_name = 'relationship_app/library_detail.html'

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(
                username = username, 
                password = password, 
                #email = email,
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'relationship_app/login.html', {'form':form})

    else:
        form = LoginForm()
               
    return render(request, 'relationship_app/login.html', {'form':form})

def register_view(request, *args, **kwargs):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']


            user = User.objects.create(
                username = username, 
                password =password, 
                email = email, 
                first_name = first_name,
                last_name = last_name,
            )
            user.set_password(password) 
            user.save()
            return redirect ('home')
    
    else:
        form =RegisterForm()

    return render (request, 'relationship_app/register.html', {'form':form})

def logout_view(request):
    #logout(request)
    return render (request, 'relationship_app/logout.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request, *args, **kwargs):
    return render(request, 'admin_view.html')
    
@user_passes_test(is_librarian)
def librarian_view(request, *args, **kwargs):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request, *args, **kwargs):
    return render(request, 'member_view.html')
    