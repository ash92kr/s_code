from django.contrib import admin
from .models import Movie, Actor, Genre, Comment

# Register your models here.
# class MovieAdmin(admin.ModelAdmin):
#     list_display =['actor1', 'poster_url', 'description', 'genre_id',] 

# admin.site.register(Movie, MovieAdmin)
    
admin.site.register(Movie)

class ActorAdmin(admin.ModelAdmin):
    list_display =['actor_id', 'name',]
                    
admin.site.register(Actor, ActorAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display =['name',]
    
admin.site.register(Genre, GenreAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'movie_id', 'content', 'score']
    
admin.site.register(Comment, CommentAdmin)