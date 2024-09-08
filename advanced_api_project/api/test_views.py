from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer

class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
    
    def test_create_book(self):
        response = self.client.post('/books/', {'title': 'New Book', 'publication_year': 2024, 'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        response = self.client.patch(f'/books/{self.book.id}/', {'title': 'Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        response = self.client.delete(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
    
    def test_filter_books(self):
        response = self.client.get('/books/?title=Harry Potter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
