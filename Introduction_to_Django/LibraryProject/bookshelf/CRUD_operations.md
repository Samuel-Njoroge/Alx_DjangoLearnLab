## CRUD Operations for Book Model.

### ✅ Create
```python

from bookshelf.models import Book

# Creating a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output:
# <Book: 1984 by George Orwell (1949)>
```

### 🔍 Retrieve
```python
# Retrieving the created Book instance
book = Book.objects.get(title="1984")
book.title
# Output: '1984'

book.author
# Output: 'George Orwell'

book.publication_year
# Output: 1949
```

## ✏️ Update
```python
# Updating the title of the Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book
# Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
```

## 🗑️ Delete
```python
# Deleting the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output:
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Output:
# <QuerySet []>
```