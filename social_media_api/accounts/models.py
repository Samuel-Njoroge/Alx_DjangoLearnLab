from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)

    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.following.add(user)
    
    def unfollow(self, user):
        """Unfollow another user"""
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()
           
    def __str__(self):
        return self.username