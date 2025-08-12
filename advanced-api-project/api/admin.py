from django.contrib import admin
from .models import Book, Author


# Author.
admin.site.register(Author)

# Book.
admin.site.register(Book)