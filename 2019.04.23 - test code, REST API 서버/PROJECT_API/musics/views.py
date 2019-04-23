from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetialSerializer       # Serializer = 특정 딕셔너리나 퀘리셋 등의 파이썬 형식 데이더 타입을 반환
from .models import Music, Artist, Comment

# Create your views here.

# response를 통해 serializer 반환
# music은 쿼리셋(일종의 리스트)인데 우리는 json으로 응답하려고 한다
# serializer가 해주는 것은 모든 리스트를 하나씩 json 타입으로 바꿔주는 도구
# Resonse는 응답하는 함수
# 결과를 보내줄 데이터는 .data로 가져온다

@api_view(['GET'])  # GET으로 요청 보냄
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetialSerializer(music)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)   # 여러 개를 보여주는 경우
    return Response(serializer.data)   # .data를 해야 json으로 보여줌

@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, music_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # 예외처리
        serializer.save(music_id=music_pk)   # 컬럼은 id
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])  # PUT이 수정, DELETE가 삭제
def comment_update_and_delete(request, music_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)  # 폼과 같다고 인식
        if serializer.is_valid(raise_exception=True):      # 수정한 내용
            serializer.save()
            return Response({'message': 'Comment has been updated'})   # 성공 메시지
    else:
        comment.delete()
        return Response({'message': 'Comment has been deleted'})

        