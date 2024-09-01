from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from bookshelf.models import CustomUser
from django.http import HttpResponseForbidden, HttpResponse
from .models import Book
# Create your views here.



@permission_required('your_app.can_view_profile', raise_exception=True)
def view_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'view_profile.html', {'user': user})

def edit_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if not request.user.has_perm('your_app.can_edit_profile'):
        return HttpResponseForbidden()
    # Logic to edit the user profile
    pass

@permission_required('your_app.can_delete_profile', raise_exception=True)
def delete_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Logic to delete the user profile
    pass

# bookshelf/views.py


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # handle form submission
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('book_detail', book_id=book.id)
    return render(request, 'bookshelf/edit_book.html', {'book': book})



def search_books(request):
    query = request.GET.get('q')
    if query:
        # Safely filter books using Django ORM
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def some_view(request):
    response = HttpResponse("Content")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trusted-scripts.example.com"
    return response