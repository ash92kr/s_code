from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-id')
    return render(request, 'movies/index.html', {'movies': movies})
    
def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movies/detail.html', {'movie': movie})

def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('/movies/')
