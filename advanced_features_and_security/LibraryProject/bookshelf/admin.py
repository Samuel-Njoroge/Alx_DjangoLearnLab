
from django.contrib import admin
from.models import Author, Book, Library, Librarian, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register the Book model.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Info"), {
            "fields": ("date_of_birth", "profile_photo",),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional Info"), {
            "fields": ("date_of_birth", "profile_photo",),
        }),
    )
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    search_fields = ("username", "email")

admin.site.register(CustomUser, CustomUserAdmin)