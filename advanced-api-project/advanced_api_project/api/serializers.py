from .models import Book, Author
from rest_framework import serializers

# Author
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'

# Book
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'