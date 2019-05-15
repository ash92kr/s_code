from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Movie, Actor, Genre, Comment
from .forms import CommentForm

# Create your views here.
def list(request):
    movies = Movie.objects.order_by('-year')[:7]
    context = {
        'movies': movies,
    }
    return render(request, 'movies/list.html', context)
    
def movie_list(request):
    movies = Movie.objects.all()
    keyword = request.GET.get('keyword', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if keyword: # q가 있으면
        movies = movies.filter(movie_name__icontains=keyword) # 제목에 q가 포함되어 있는 레코드만 필터링
    context = {
        'movies': movies
    }
    return render(request, 'movies/movie_list.html', context)
    
# def contact(request):
#     return render(request, 'movies/contact.html')
    
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    actors = get_list_or_404(Actor.objects.order_by('-pk'))
    context = {
        'movie': movie,
        'actors': actors,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
@login_required    
def comment_create(request, movie_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id = request.user.id
        comment.movie_id = movie_pk
        # comment.movie = movie_pk
        comment.save()
    return redirect('movies:detail', movie_pk)


@require_POST
@login_required
def comment_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)
    

@login_required
def comment_update(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if comment.user == request.user:
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:detail', movie_pk)
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('movies:detail', movie_pk)
    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'movies/detail.html', context)
    
        