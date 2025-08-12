from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets, permissions, filters 
from rest_framework import generics
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

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

    # Filter, Search, Order
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

       # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

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
