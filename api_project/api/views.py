from django.shortcuts import render
from .models import Book
from .serializers import BookSerilizer
from rest_framework import generics, viewsets

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer