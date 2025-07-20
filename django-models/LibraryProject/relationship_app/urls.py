from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomeLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library'),

]