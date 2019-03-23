from django.shortcuts import render, redirect, get_object_or_404
from .models import Genre, Movie, Score
from .forms import MovieForm, ScoreForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
    
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # audience = form.cleaned_data.get('audience')
            # poster_url = form.cleaned_data.get('poster_url')
            # description = form.cleaned_data.get('description')
            # genre = form.cleaned_data.get('genre')
            # movie = Movie.objects.create(title=title, audience=audience, poster_url=poster_url, description=description, genre=genre)
            # movie.save()
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movies/form.html', context)
        
        
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
    
    
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie_pk)
    

def edit(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            # movie.title = form.cleaned_data.get('title')
            # movie.audience = form.cleaned_data.get('audience')
            # movie.poster_url = form.cleaned_data.get('poster_url')
            # movie.description = form.cleaned_data.get('description')
            # movie.genre_id = form.cleaned_data.get('genre')
            # movie.save()
            movie = form.save()
            return redirect('movies:detail', movie_pk)
    else:
        form = MovieForm(instance=movie)
    context = {'form': form, 'movie': movie,}
    return render(request, 'movies/form.html', context)
        