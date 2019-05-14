from django.db import models
from django.conf import settings
        
class Actor(models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
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
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actor1 = models.IntegerField()
    actor2 = models.IntegerField()
    actor3 = models.IntegerField()
    poster_url = models.TextField()
    link_url = models.TextField()
    user_rating = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.movie_name
                                
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    
    def __str__(self):
        return self.content


# Create your models here.
# class Hashtag(models.Model):
#     content = models.TextField(unique=True)
    
#     def __str__(self):
#         return self.content