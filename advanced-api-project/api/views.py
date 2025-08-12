from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets, generics, permissions

# Author
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve all the books.
class BookListView(generics.ListAPIView):
    """List all books to authenticated and unauthenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """Retrieve a single book by its ID to authenticated and unauthenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Add a new book.
class BookCreateView(generics.CreateAPIView):
    """Create a new book accessible to authenticated users only."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Modify an  existing book
class BookUpdateView(generics.UpdateAPIView):
    """Update a book accessible to authenticated users only."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 

# Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """Delete book accessible to authenticated users only."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
