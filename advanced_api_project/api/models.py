from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title} -- publication year is {self.publication_year}, author is -- {self.author}'