from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.delete_book, name = 'delete'),
    path('edit_book/', views.change_book, name = 'change'),
    path('add_book/', views.add_book, name = 'add'),
    path('memberv/', views.member_view, name = 'member'),
    path('librarianv/', views.librarian_view, name = 'librarian'),
    path('adminv/', views.admin_view, name = 'admin'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name = 'library_detail'),
    path('lists/', views.list_books, name = "list_books"),
    path('', views.home, name = "home"),
]