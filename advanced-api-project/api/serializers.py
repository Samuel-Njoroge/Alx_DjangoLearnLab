from .models import Book, Author
from django.utils import timezone
from rest_framework import serializers


# Book
class BookSerializer(serializers.ModelSerializer):
    """Custom validation to ensure publication_year is not set in the future."""
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    

# Author
class AuthorSerializer(serializers.ModelSerializer):
    """Includes author's name and nested list of their books."""
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']