from django.shortcuts import render
from .models import Book
from .serializers import BookSerilizer
from rest_framework import viewsets
from rest_framework import generics

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)

        if name_filter is not None:
            queryset =queryset.filter(name__icontains=name_filter)

        return queryset

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer