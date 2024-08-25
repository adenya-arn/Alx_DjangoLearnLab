from django.urls import path
from .views import list_books, LibraryDetailView
from .views import add_book, edit_book, delete_book, list_books, user_login, user_logout, user_register

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('book/add/', add_book, name='add_book'),
    path('book/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', delete_book, name='delete_book'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
]

