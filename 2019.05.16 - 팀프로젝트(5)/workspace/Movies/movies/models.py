from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator        

class Actor(models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
        
class Genre(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name = models.TextField()
    time = models.IntegerField()
    year = models.IntegerField()
    nation = models.TextField()
    director = models.TextField()
    company = models.TextField()
    grade = models.TextField()
    actor1 = models.IntegerField(blank=True)
    actor2 = models.IntegerField(blank=True)
    actor3 = models.IntegerField(blank=True)
    poster_url = models.TextField()
    link_url = models.TextField()
    user_rating = models.IntegerField()
    description = models.TextField()
    film_url = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    # score_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='score_movies', through='Comment')
    
    def __str__(self):
        return self.actor1
                                
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    def __str__(self):
        return self.content
