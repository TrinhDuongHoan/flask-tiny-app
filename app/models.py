from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
