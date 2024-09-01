from .serializers import BookSerializer
from django.shortcuts import render
import rest_framework.generics
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import rest_framework


# Create your views here.

class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

"""  def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)

        if name_filter is not None:
            queryset =queryset.filter(name__icontains=name_filter)

        return queryse"""

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]