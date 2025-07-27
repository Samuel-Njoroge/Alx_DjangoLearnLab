# A simple Library application.


### Admin Registration
The `Book` model is registered in `bookshelf/admin.py` with a customized admin interface:

- `list_display`: Shows title, author, and publication year.
- `list_filter`: Allows filtering by author and publication year.
- `search_fields`: Enables searching by title and author.

### Access
Start the server with:
```bash
python manage.py runserver
```