from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator   # 최소값, 최대값 범위 지정
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
        
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='score_movies', through='Score')
    # 다대다 관계의 연결 테이블(여러 유저 - 점수 - 여러 영화)

class Score(models.Model):
    content = models.CharField(max_length=200)
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    