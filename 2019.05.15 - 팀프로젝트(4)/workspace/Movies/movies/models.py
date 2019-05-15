from django.db import models
from django.conf import settings
        
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
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.actor1
                                
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    
    def __str__(self):
        return self.content
