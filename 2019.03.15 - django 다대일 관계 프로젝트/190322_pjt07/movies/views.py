from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Genre, Movie, Score

# Create your views here.
def index(request):
    # movies = Movie.objects.order_by('-pk')
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
    # db에 반영되지 않고 가상의 컬럼이 새롭게 만들어져서 출력된다(migrate 필요 없음)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
    
def detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)   # 왼쪽에 join을 해서 붙인다
    genre = Genre.objects.get(pk=movie.genre_id)   # 바로 위의 movie를 받음
    scores = movie.score_set.all()  # 각 영화에 달린 모든 댓글 보여주기
    context = {
        'movie': movie,
        'genre': genre,
        'scores': scores,
    }
    return render(request, 'movies/detail.html', context)
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    if request.method == "POST":
        movie.delete()
        # return redirect('/movies/')
    # else:
        # return redirect('/movies/')
    return redirect('movie:index')    
    
def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    content = request.POST.get('content')
    score = request.POST.get('score')
    
    comment = Score(movie=movie, content=content, score=score)  # movie도 받아와야 한다
    comment.save()
    return redirect('movie:detail', movie.pk)
    
def comments_delete(request, movie_pk, score_pk):
    comment = Score.objects.get(pk=score_pk)
    
    if request.method == "POST":
        comment.delete()
    
    return redirect('movie:detail', movie_pk)
