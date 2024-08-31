from django.contrib import admin
from .models import Author, Librarian, Library, Book, UserProfile, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(UserProfile)
admin.site.register(CustomUser, UserAdmin)