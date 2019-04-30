[TOC]

## Django_13_REST_API

**Content**

0. 준비하기
1. Model
2. Music List
3. Music Detail
4. API Document
5. Artist List
6. Artist Detail
7. Create Comment
8. Update and Delete Comment

> 190423 /  Tue

---

### 0. 준비하기

> [Django REST framework](https://www.django-rest-framework.org/)

```bash
$ django-admin startproject api .
```

```bash
$ pip install djangorestframework
```

```python
# api/settings.py
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'rest_framework',
  ...
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_TZ = False
```

```bash
$ python manage.py startapp musics
```

```python
# api/settings.py
INSTALLED_APPS = [
    'musics.apps.MusicsConfig',
  ...
]
```

---

### 1. Model

- Artist / Music / Comment 3개의 모델을 만든다.

```python
# movies/models.py
from django.db import models

class Artist(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.TextField()
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- admin 계정을 미리 만들고 **실습을 위한 데이터들을 미리 넣어 놓는다.** ( ex. 가수 2명 / 가수당 노래 2개 / 노래당 댓글 2개)

```bash
$ python manage.py createsuperuser
```

```python
# movies/admin.py
from .models import Artist, Music, Comment

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Comment)
```

---

### 2. Music List

- 아래와 같이 URL 을 설정하는 이유는 모든 모델들에 대한 정보를 표현할 것이기 때문에, `musics/` 로 시작하지 않는다.

- 일반적인 API들은 URL을 이렇게 버전을 명시해서 작성한다.

  ```python
  # api/urls.py
  from django.urls import path, include
  
  urlpatterns = [
      path('api/v1/', include('musics.urls')), 
  		...
  ]
  ```

  ```python
  # musics/views.py
  from .models import Music
  
  def music_list(request):
      musics = Music.objects.all()
  ```

  ```python
  # musics/urls.py
  from . import views
  
  urlpatterns = [
      path('musics/', views.music_list),
  ]
  ```

  ```python
  # musics/views.py
  from .models import Music
  
  def music_list(request):
      musics = Music.objects.all()
  ```

- 여기까지는 평소에 만들던 방식과 동일하다.

- 그런데, 요청 들어 오는 것과 반환하는 방식이 다르다.

- 먼저 요청 들어온 것은 다음과 같이 어떠한 HTTP method 대해서 처리할 것인지 정의한다.

  ```python
  # musics/views.py
  from rest_framework.decorators import api_view
  
  @api_view(['GET'])
  def music_list(request):
      musics = Music.objects.all()
  ```

- 다음으로,  REST Framework에서는 리턴 값이 다르다. 기존에는 `render` 함수를 통해 HTML(템플릿)을 반환하지만 API에서는 `Response`를 통해 `Serializer` 를 반환한다.

- 사용자에게 보기 편한 응답이 아니라 데이터만 주는 것으로, json 형식을 활용해서 반환한다.

- 특정한 dictionary 혹은 queryset 등의 파이썬 형식의 데이터 타입을 반환하도록 해주는 것이 Serializer이다.

- `serializer.py`

  - 새로운 것이지만, 구조는 `ModelForm` 과 굉장히 유사하다.

  ```python
  # musics/serializers.py
  from rest_framework import serializers
  from .models import Music
  
  class MusicSerializer(serializers.ModelSerializer):
      class Meta:
          model = Music
          fields = ['id', 'title', 'artist',]
  ```

  ```python
  # musics/views.py
  from rest_framework.response import Response
  from .serializers import MusicSerializer
  
  @api_view(['GET'])
  def music_list(request):
      musics = Music.objects.all()
      serializer = MusicSerializer(musics, many=True)
      return Response(serializer.data)
  ```

- 만든 것을 가져오고, 내가 보내줄 `musics` 를 넣고, `many=True` 를 설정하자.

- 이를 설정하는 이유는 동일한 유형의 **데이터(Music 인스턴스)의 집합**이므로 설정하는 것이다.

- `musics` 는 queryset, 즉 일종의 리스트인데 우리가 응답하려고 하는 것은 `json`이다. 따라서 `Serializer`가 해주는 것은 리스트를 하나 하나씩 `json` 타입으로 바꿔주는 고마운 도구이다.

- 그리고 응답하는 함수도 다른데 `REST Framework`에서 사용하는 `Response` 를 사용한다.

- 결과로 보내줄 데이터는 `.data` 로 가져온다. 

  > `<class 'rest_framework.utils.serializer_helpers.ReturnList'>` : `Many=True`

- 이제 직접 확인해보자.

  ```
  https://example.c9users.io/api/v1/musics/
  ```

---

### 3. Music Detail

```python
# musics/views.py
from django.shortcuts import render, get_object_or_404

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
```

```python
# musics/urls.py
path('musics/<int:music_pk>/', views.music_detail),
```

- music 은 결과가 하나의 인스턴스이다. 리스트가 아니라서, `many=True` 는 쓰지 않아도 된다.

  > `<class 'rest_framework.utils.serializer_helpers.ReturnDict'>`

- `many=True` 차이를 보면 아래와 같다. list 와 detail 의 결과를 각각 보면 시작이 list 와 dictionary 이다.

  ```json
  // /api/v1/musics/
  [
      {
          "id": 1,
          "title": "yellow",
          "artist": 1
      },
      {
          "id": 2,
          "title": "everglow",
          "artist": 1
      }
  ]
  ```

  ```json
  // /api/v1/musics/1/
  
  {
      "id": 1,
      "title": "yellow",
      "artist": 1
  }
  ```

---

### 4. API Document

- 이렇게 직접 URL 을 확인하면서 들어가는 것이 불편한데, 보통 API는 문서화를 해서 어떤 주소가 어떤 역할을 하는지 정리해 놓는다. 그리고 이 문서화를 해주는 라이브러리가 있다. 가장 범용적으로 사용되는 `swagger` 를 사용해보자.

  ```bash
  $ pip install django-rest-swagger
  ```

  ```python
  # settings.py
  INSTALLED_APPS = [
  		...
      'rest_framework',
      'rest_framework_swagger',
  		...
  ]
  ```

  ```python
  # musics/urls.py
  from rest_framework_swagger.views import get_swagger_view
  
  path('docs/', get_swagger_view(title='Api Docs')),
  ```

- `/api/v1/docs/` 로 접속해서 확인하면, ~~예쁜~~ API 문서가 나타난다.

---

### 5. Artist List

```python
# musics/serializers.py
from .models import Music, Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name',]
```

```python
# musics/views.py
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
```

```python
# musics/urls.py
path('artists/', views.artist_list),
```

---

### 6. Artist Detail

```python
# musics/views.py
@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)
```

```python
# musics/urls.py
path('artists/<int:artist_pk>/', views.artist_detail),
```

- 확인해보면 artist 가 가지고 있는 music 이 출력되지 않는다. music에는 artist 정보가 있지만, artist에는 music 정보가 없다.

- 생각해보면 당연하다. 1:N 관계에서 실제 데이터베이스에는 N인 music 에만 artist의 pk 값이 저장되어 있을 뿐이기 때문이다.

- Serializer 부터 바꿔야한다. Serializer는 데이터의 형식을 지정해주는 것과 동일한데, 기존의 Artist 오브젝트에 추가적인 내용이 필요하기 때문이다.

  ```python
  # musics/serializers.py
  class ArtistDetailSerializer(serializers.ModelSerializer):
      music_set = MusicSerializer(many=True)
      class Meta:
          model = Artist
          fields = ['id', 'name', 'music_set',] 
  ```

  ```python
  # musics/views.py
  from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer
  
  @api_view(['GET'])
  def artist_detail(request, artist_pk):
      artist = get_object_or_404(Artist, pk=artist_pk)
      serializer = ArtistDetailSerializer(artist)
      return Response(serializer.data)
  ```

- 다시 artist detail 로 요청을 보내보면, 해당 artist 의 music 들도 같이 응답으로 주는 것을 확인할 수 있다.

> `music_set` 이 아닌 다른 이름으로 사용하고 싶다면,
>
> 1. models.py 에서 related_name 설정
> 2. serializers 에서 직접 설정
>
> 2가지 방법이 있다. 2번째 방법을 보여주자면
>
> ```python
> # musics/serializers.py
> class ArtistDetailSerializer(serializers.ModelSerializer):
>     musics = MusicSerializer(source='music_set', many=True)
>     class Meta:
>         model = Artist
>         fields = ['id', 'name', 'musics',]  
> ```
>
> - 오류가 뜬다면 서버를 재시작하자.

---

### 7. Create Comment

- 데이터를 가져오는 것 말고도 직접 생성을 해보자.

- 생성은 POST 요청이어야 한다.

  ```python
  # musics/serializers.py
  from .models import Music, Artist, Comment
  
  class CommentSerializer(serializers.ModelSerializer):
      class Meta:
          model = Comment
          fields = ['id', 'content',]
  ```

  ```python
  # musics/views.py
  from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
  
  @api_view(['POST'])
  def comment_create(request, music_pk):
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(music_id=music_pk)
          return Response(serializer.data)
  ```

  ```python
  # musics/urls.py
  path('musics/<int:music_pk>/comments/', views.comment_create),
  ```

  >  `raise_exception=True` 는 검증되지않으면  `400 Bad Request` 오류를 발생시킨다.
  >
  > ```python
  > # 아래 코드를 짧게 설정한 것이다.
  > if not serializer.is_valid():
  > 	raise ValidationError(serializer.errors)
  > ```

- Postman 을 사용해서 테스트를 해보자. (**POST 요청은 url 마지막에 반드시 `/` 가 있어야한다.**)

- Post 로 전달할 데이터는 postman에  `body` 에 작성해서 보내야한다.

- Music Detail에서 Comment도 나오게 하려면, Artist Detail에서 Music을 나오게한 방법을 그대로 사용하면 된다.

  ```python
  # musics/serializers.py
  class MusicDetailSerializer(serializers.ModelSerializer):
      comment_set = CommentSerializer(many=True)
      class Meta:
          model = Music
          fields = ['id', 'title', 'artist', 'comment_set',]
  ```

  ```python
  # musics/views.py
  from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer
  
  @api_view(['GET'])
  def music_detail(request, music_pk):
      music = get_object_or_404(Music, pk=music_pk)
      serializer = MusicDetailSerializer(music)	# 변경
      return Response(serializer.data)
  ```

---

### 8. Update and Delete Comment

- 같은 주소로 다른(PUT, DELETE) method 로 요청을 보내면 서로 다른 요청으로 인식하여, 수정 삭제를 같은 주소로 구현해보자.

- 수정은 `PUT`, 삭제는 `DELETE` method를 사용한다.

  ```python
  # musics/views.py
  @api_view(['PUT', 'DELETE'])
  def comment_update_and_delete(request, music_pk, comment_pk):
      comment = get_object_or_404(Comment, pk=comment_pk)
      if request.method == 'PUT':
          serializer = CommentSerializer(data=request.data, instance=comment)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              return Response({'message': 'Comment has been updated!!'})
      else:
          comment.delete()
          return Response({'message': 'Comment has been deleted!!'})
  ```

  ```python
  # musics/urls.py
  path('musics/<int:music_pk>/comments/<int:comment_pk>/', views.comment_update_and_delete)
  ```

- PUT, DELETE 도 POST 와 마찬가지로 Postman 에서 테스트를 해보자.

- 수정 및 삭제 요청을 보내보고 admin 페이지에서 잘 삭제되었는지 확인해본다.

---

### 9. 부록

- artist 가 가지고 있는 모든 music 개수 데이터 만들기

```python
# musics/serializers.py
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    music_count = serializers.IntegerField(source='music_set.count')
    class Meta:
        model = Artist
        fields = ['id', 'name', 'music_set', 'music_count',]    
```



