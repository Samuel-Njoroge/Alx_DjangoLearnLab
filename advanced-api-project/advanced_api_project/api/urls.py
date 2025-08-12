from .views import BookViewSet, AuthorViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Router
router = DefaultRouter()

# Routes
router.register('book', BookViewSet, basename='book')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]