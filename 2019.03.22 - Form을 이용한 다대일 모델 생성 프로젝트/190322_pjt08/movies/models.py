from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}, {self.audience}, {self.poster_url}, {self.description}'
        
class Score(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.content}, {self.score}'