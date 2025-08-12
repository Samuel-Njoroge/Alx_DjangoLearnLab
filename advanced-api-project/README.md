#  Book Views

## Endpoints
- `GET /books/` – List all books (public)
- `GET /books/<id>/` – Retrieve a single book (public)
- `POST /books/create/` – Create a new book (auth required)
- `PUT /books/<id>/update/` – Update a book (auth required)
- `DELETE /books/<id>/delete/` – Delete a book (auth required)

## Permissions
- Read operations (`GET`) are public.
- Write operations (`POST`, `PUT`, `DELETE`) require authentication.

## Notes
- Nested author serialization is handled in the `AuthorSerializer`.
- `BookSerializer` enforces that `publication_year` cannot be in the future.
- Additional filters can be applied via query params in `BookListView`.
