from django.contrib import admin
from .models import Movie, Actor, Genre

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display =['movie_name', 'time', 'year', 'nation', 'director', 'company',]
                    
admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display =['actor_id', 'name',]
                    
admin.site.register(Actor, ActorAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display =['name',]
                    
admin.site.register(Genre, GenreAdmin)