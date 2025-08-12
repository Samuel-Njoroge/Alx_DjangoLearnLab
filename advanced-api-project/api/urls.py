from .views import BookViewSet, AuthorViewSet, BookListView, BookCreateView, BookUpdateView, BookDetailView, BookDeleteView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Router
router = DefaultRouter()

# Routes
router.register('book', BookViewSet, basename='book')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]