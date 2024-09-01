from django.contrib import admin

from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)



