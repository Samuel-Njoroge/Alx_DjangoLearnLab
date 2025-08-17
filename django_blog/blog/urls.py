from django.urls import path
from .views import home, register, profile, UserLoginView, UserLogoutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_comment, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path("", home, name="home"),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path("posts/<int:post_id>/comments/new/", add_comment, name="add-comment"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile",)
]