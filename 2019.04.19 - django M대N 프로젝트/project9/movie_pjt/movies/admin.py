from django.contrib import admin
from .models import Movie, Genre
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'poster_url', 'description',)
    
admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Genre, GenreAdmin)