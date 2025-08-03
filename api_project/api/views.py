from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


# BookList View
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
