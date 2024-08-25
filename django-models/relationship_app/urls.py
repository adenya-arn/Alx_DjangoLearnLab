from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("lists/", views.books_in_library_view,name="lists"),
    path("details/", views.Library_Detail, name = "details")
]