from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, blank=True)
    introduction = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=40, blank=True)
    
    def __str__(self):
        return self.nickname

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    
