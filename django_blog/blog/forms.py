from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


# User Creation Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Post 
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
# Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment here..."})
        }