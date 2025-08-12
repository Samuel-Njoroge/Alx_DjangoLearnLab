from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create authors and books
        self.author1 = Author.objects.create(name="Ngef")
        self.author2 = Author.objects.create(name="Kafla")

        self.book1 = Book.objects.create(
            title="Apache Kafka",
            publication_year=2020,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Apache Spark",
            publication_year=2023,
            author=self.author1
        )
        self.book3 = Book.objects.create(
            title="Apache Iceberg",
            publication_year=2024,
            author=self.author2
        )

        self.book_list_url = reverse('book-list') 

    def test_list_books(self):
        """Ensure that the list endpoint returns all books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        """Authenticated user can create a book."""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Apache Trino",
            "publication_year": 2024,
            "author": self.author1.id
        }
        url = reverse('book-create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        """Unauthenticated user cannot create a book."""
        data = {
            "title": "Apache Trino",
            "publication_year": 2024,
            "author": self.author1.id
        }
        url = reverse('book-create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Authenticated user can update a book."""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            "title": "Apache Airflow",
            "publication_year": 2020,
            "author": self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Apache Airflow")

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book."""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', kwargs={'pk': self.book1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_author(self):
        """Filter books by author ID."""
        response = self.client.get(f"{self.book_list_url}?author={self.author1.id}")
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        """Search books by title."""
        response = self.client.get(f"{self.book_list_url}?search=Brave")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Brave New World")

    def test_order_books_by_year(self):
        """Order books by publication year."""
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
