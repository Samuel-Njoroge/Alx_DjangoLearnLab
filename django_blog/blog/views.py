from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, PostForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

# List view
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ['-published_date']
    paginate_by = 10

# Detail view
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Create - Authenticated users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Update 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user 
    
# Delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object
        return post.author == self.request.user 