from .views import BookList, BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Router 
router = DefaultRouter()

# Routes
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)), 
    path('token/', obtain_auth_token, name='api-token'),
]