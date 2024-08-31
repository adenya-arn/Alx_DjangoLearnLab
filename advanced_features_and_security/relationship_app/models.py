from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)

    class Meta:
        permissions= [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__ (self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__ (self):
        return self.name

class Librarian(models.Model):
    name =models.CharField(max_length=100)
    library =  models.OneToOneField(Library, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(
                            max_length=50,
                            choices=[
                                ('Admin', 'Admin'),
                                ('Librarian', 'Librarian'),
                                ('Member', 'Member'),
                             ]
                        )
    def __str__(self):
        return f'{self.user.username} - {self.role}'
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    def __str__(self):
        return self.date_of_birth

