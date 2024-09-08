from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields = '__all__'

    def validate_publications_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publiction year cannot be in the future")
        
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']