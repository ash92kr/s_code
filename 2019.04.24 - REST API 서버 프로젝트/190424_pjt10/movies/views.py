from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, GenreDetailSerializer, MovieSerializer, ScoreSerializer
from .models import Genre, Movie, Score

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def score_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)    # 이 코드를 넣어야 영화 pk가 없으면 404에러가 난다
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)   # movie_id 컬럼에 movie_pk가 들어간다
        return Response({'message': '작성되었습니다.'})

@api_view(['PUT', 'DELETE'])
def score_update_and_delete(request, score_pk):
    score = get_object_or_404(Score, pk=score_pk)   # 평점이 없으면 404에러
    if request.method == "PUT":
        serializer = ScoreSerializer(data=request.data, instance=score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        score.delete()
        return Response({'message': '삭제되었습니다.'})
        
        