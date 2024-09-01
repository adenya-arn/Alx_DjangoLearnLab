
import rest_framework.serializers
from .models import Book
import rest_framework
class BookSerilizer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'