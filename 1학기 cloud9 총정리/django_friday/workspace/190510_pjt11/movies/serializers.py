from rest_framework import serializers
from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name',]   # 'id'나 'name'은 필드명에 불과하므로 내 마음대로 이름 지정 가능

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score',]

class MovieSerializer(serializers.ModelSerializer):
    score_set = ScoreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre', 'score_set',]

class GenreDetailSerializer(serializers.ModelSerializer):
    movie_set = MovieSerializer(many=True)   # 이를 넣기 전에 먼저 선언해야 한다
    class Meta:
        model = Genre
        fields = ['id', 'name', 'movie_set',]  # movie_set 자체가 하나의 쿼리셋이므로 이중 쿼리셋이 됨

