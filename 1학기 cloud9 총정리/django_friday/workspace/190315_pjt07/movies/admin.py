from django.contrib import admin
from .models import Genre, Movie, Score

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'poster_url', 'description', 'genre_id',)
    
admin.site.register(Movie, MovieAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('content', 'score', 'movie_id',)
    
admin.site.register(Score, ScoreAdmin)