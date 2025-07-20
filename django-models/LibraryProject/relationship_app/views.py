from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# List all the books stored in the database.
def list_books(request):
    """List books: title, author"""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    template_name =  'relationship_app/library_detail.html'