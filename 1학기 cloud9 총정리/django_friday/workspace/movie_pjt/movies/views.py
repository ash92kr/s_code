from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Movie, Score
from .forms import ScoreForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    scores = Score.objects.all()
    context = {
        'movies': movies,
        'scores': scores,
    }
    return render(request, 'movies/list.html', context)

    
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ScoreForm()
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)
    

@require_POST
@login_required
def score_create(request, movie_pk):  # 특정 영화에 평점을 준다
    movie = get_object_or_404(Movie, pk=movie_pk)  
    form = ScoreForm(request.POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.user = request.user
        score.movie_id = movie_pk   # movie 변수에 기본키가 들어감
        score.save()
        return redirect('movies:detail', movie_pk)
    return redirect('movies:list')


@require_POST
@login_required
def score_delete(request, movie_pk, score_pk):
    score = get_object_or_404(Score, pk=score_pk)
    if request.user != score.user:
        return redirect('movie:list')
    score.delete()
    return redirect('movies:detail', movie_pk)


    