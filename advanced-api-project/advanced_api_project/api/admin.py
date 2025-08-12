from django.contrib import admin
from .models import Book, Author


# Author.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

# Book.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'author')
    search_fields = ('title',)
    list_filter = ('author',)