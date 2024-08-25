"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from relationship_app.views import add_book, edit_book, delete_book


urlpatterns = [
    path("", include('relationship_app.urls')),
    path("lists/", include('relationship_app.urls')),
    path("details/", include('relationship_app.urls')),
    path('admin/', admin.site.urls),


    path('book/add/', add_book, name='add_book'),
    path('book/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', delete_book, name='delete_book'),
]
