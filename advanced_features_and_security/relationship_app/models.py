from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
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

    class Meta:
        permissions= [
            ("can_view", "Can view "),
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
            ("can_edit", 'Can edit book'),
        ]

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
    


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(null=True, blank=True)

    objects = CustomUserManager()
    def __str__(self):
        return self.date_of_birth
