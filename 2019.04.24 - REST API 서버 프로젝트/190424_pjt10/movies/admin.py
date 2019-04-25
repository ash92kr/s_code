from django.contrib import admin
from .models import Movie, Genre, Score

# Register your models here.

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['title', 'audience', 'poster_url', 'description',]

# admin.site.register(Movie, MovieAdmin)

# class GenreAdmin(admin.ModelAdmin):
#     list_display = ['name']
    
# admin.site.register(Genre, GenreAdmin)

# class ScoreAdmin(admin.ModelAdmin):
    # list_display = ['content', 'score',]

# admin.site.register(Score, ScoreAdmin)

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Score)