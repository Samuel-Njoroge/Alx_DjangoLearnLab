from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. All books by a specific Author
    author_name = "George Orwell"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}")
        for book in books_in_library:
            print(f" - {book.title} by {book.author.name}")

    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # 3. Retrieve the librarian for a library
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"No librarian found for {library_name}")        
