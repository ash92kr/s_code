from django.shortcuts import reverse
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    
    def get_absolute_url(self):  # 특정 사람의 프로필 정보로 이동
        return reverse("accounts:detail", args=[self.pk])