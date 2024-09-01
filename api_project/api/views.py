from django.shortcuts import render
import rest_framework.generics
from .models import Book
from .serializers import BookSerilizer
from rest_framework import viewsets
from rest_framework import generics
import rest_framework
# Create your views here.

class BookList(rest_framework.generics.ListAPIView):
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