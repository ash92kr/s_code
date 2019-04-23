from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id','title', 'artist',]  # json 파일의 모든 열 보기

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name',]

class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)   # 쿼리셋이므로 many를 써야 한다
    class Meta:
        model = Artist
        fields = ['id', 'name', 'music_set',]
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content',]

class MusicDetialSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'comment_set',]