from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from .models import Post


# Registration
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
        
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# Profile
@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.save()
        return render(request, "blog/profile.html", {"success": True})
    return render(request, "blog/profile.html")

# Login & Logout
class UserLoginView(LoginView):
    template_name = "blog/login.html"

class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"


def home(request):
    return render(request, "blog/home.html")

def posts(request):
    all_posts = Post.objects.all().order_by("-published_date")  # newest first
    return render(request, "blog/posts.html", {"posts": all_posts})