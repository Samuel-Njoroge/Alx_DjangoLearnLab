from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# User Registration
class RegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# User Login
class CustomeLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# User Logout
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# List all the books stored in the database.
@login_required
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

