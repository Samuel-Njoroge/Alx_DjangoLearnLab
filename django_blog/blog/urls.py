from django.urls import path
from .views import posts, home, register, profile, UserLoginView, UserLogoutView


urlpatterns = [
    path("", home, name="home"),
    path("posts/", posts, name="posts"),
    path("register/", register, name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile",)
]