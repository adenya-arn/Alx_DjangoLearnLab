from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name = 'library_detail'),
    path('lists/', views.list_books, name = "list_books"),
    path('', views.home, name = "home"),
]