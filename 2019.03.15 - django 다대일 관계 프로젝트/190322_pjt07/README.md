# 2019.03.15



pjt_07

프로젝트 폴더 : crud

app 폴더 : movies

평점/평균은 마지막에 다같이 할 예정 -> 기능 구현부터, 디자인은 나중에



## 1. workspace 설정 및 설치

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
pyenv rehash
```



```
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
```



```
python -V
pip install -U pip
pip install flask
pip install requests
pip freeze > req.txt
```



```
pyenv virtualenv 3.6.7 django-venv
```



```
mkdir 190322_pjt07
cd 190322_pjt07
pyenv local django-venv
```



```
pip install django
pip install --upgrade pip
```



```
django-admin startproject crud .
python manage.py startapp movies

# .gitignore 파일 설정
```



* settings.py

```
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'movies.apps.MoviesConfig',
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_TZ = False
```





## 2. 모델 설정



* models.py

```
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} : {self.audience} : {self.poster_url} : {self.description}"
        
class Score(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.content} : {self.score}"
```



```
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```



## 3. 데이터 넣기



* movies.csv와 genre.csv를 프로젝트 디렉토리에 넣은 다음, 헤더(id 등)를 삭제함

```
sqlite3 db.sqlite3     # 그냥 sqlite3만 입력하면 매번 빈 프로그램에서 실시하는 것
.mode csv
.import genre.csv movies_genre
.import movie.csv movies_movie
.tables
.exit
```



* admin.py

```
from django.contrib import admin
from .models import Genre, Movie, Score
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'poster_url', 'description', 'genre_id',)
    
admin.site.register(Movie, MovieAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('content', 'score', 'movie_id',)
    
admin.site.register(Score, ScoreAdmin)
```



```
python manage.py createsuperuser
```



## 4. Movies CRUD 만들기



* crud - urls.py

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]
```



* movies - urls.py

```
from django.urls import path

urlpatterns = [

]
```





### (1) 영화 목록



* views.py

```
def index(request):
    return render(request, 'movies/index.html')
```



```
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
```



* urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```



* base.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{% block title %} {% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    {% block style %} {% endblock %}
</head>
<body>
    {% block body %}
    
    {% endblock %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```



* index.html

```
{% extends 'movies/base.html' %}

{% block title %} INDEX  {% endblock %}

{% block body %}
    <h1>영화 목록</h1>
    <br>

    {% for movie in movies %}
        <div class="container">
            <h3><a href="/movies/{{movie.id}}/">{{ movie.title }}</a></h3>
            <img src="{{ movie.poster_url }}"></img>
            <hr>
        </div>
    {% endfor %}

{% endblock %}
```



### (2) 영화 정보 조회

* views.py

```
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    genre = Genre.objects.get(pk=movie.genre_id)
    context = {
        'movie': movie,
        'genre': genre,
    }
    return render(request, 'movies/detail.html', context)
```



* urls.py

```
    path('<int:pk>', views.detail, name='detail'),
```



* detail.html

```
{% extends 'movies/base.html' %}

{% block title %} DETAIL {% endblock %}

{% block body %}

    <div class="container">
        <h1>영화 정보 조회</h1>
        
        <hr>
        
        <p><h3>영화명 : {{ movie.title }}</h3></p>
        <p><h3>관객수 : {{ movie.audience }}</h3></p>
        <p>포스터 : <img src="{{ movie.poster_url }}"></img></p>
        <p>설명 : {{ movie.description }}</p>
        <p>장르 : </p>
        
        <hr>
        
        <a href="/movies/">[목록]</a>
        <a href="#">[수정]</a>   # 수정은 버튼만 만듦!
        <a href="#">[삭제]</a>
        
    </div>

{% endblock %}
```



### (3) 영화 정보 삭제

* views.py

```
from django.shortcuts import render, redirect

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    if request.method == "POST":
        movie.delete()
        return redirect('/movies/')
    else:
        return redirect('/movies/')
```



* urls.py

```
    path('<int:pk>/delete/', views.delete, name='delete'),
```



* detail.html

```
        <form method="POST" style="display:inline">
            {% csrf_token %}
            <input type="submit" value="삭제"/>
        </form>
```



## 5. RESTful 및 url_name 적용하기



* settings.py

```
INSTALLED_APPS = [
    'movies.apps.MoviesConfig',
    'django_extensions',
]
```



```
pip install django_extensions
```



* urls.py

```
app_name = 'movie'   # 이제 urls를 거친 정보는 모두 movie로 바꿔야 한다(뷰함수의 기본키, html에서 url의 ' ' 안에 있는 내용)
```



* views.py

```
    return redirect('movie:index')
```



* index.html

```
            <h3><a href="{% url 'movie:detail' movie.pk %}">{{ movie.title }}</a></h3>
```



* detail.html

```
        <a href="{% url 'movie.index' %}">[목록]</a>
        
        <form action="{% url 'movie:delete' movie.pk %}" method="POST" style="display:inline">
```



### 6. 댓글(Score) CRUD



* views.py - movies와 score의 pk를 구분하기 위해 _을 붙인다

```
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
```



* urls.py

```
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/', views.detail, name='detail'),
```



### (1)  평점 생성



* views.py

```
def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    content = request.POST.get('content')
    score = request.POST.get('score')   # 사용자가 입력한 점수를 받음(score 변수)
    
    comment = Score(movie=movie, content=content, score=score)  # movie 객체를 받아오면 그 중 movie.id가 Score 객체에 저장된다(score변수를 score 컬럼에 넣음)
    comment.save()
    return redirect('movies:detail', movie.pk)
```



* urls.py

```
    path('<int:movie_pk>/scores/new/', views.comments_create, name='comments_create'),
```



* detail.html

```
        <form action="{% url 'movie:comments_create' movie.pk %}" method="POST">
            {% csrf_token %}    <!--comments_create 함수에 movie.pk를 보낸다-->
            <label for="content">내용:</label>
            <input type="text" name="content" id="content"/>
            <label for="score">평점:</label>
            <input type="number" name="score" id="score"/>
            <input type="submit" value="평점 주기"/>
        </form>
```



### (2) 평점 조회



* urls.py

```
    scores = movie.score_set.all()  # 각 영화에 달린 모든 댓글 보여주기(score 테이블의 모든 객체 가져옴)
    context = {
        'movie': movie,
        'genre': genre,
        'scores': scores,    # detail.html에 보내는 값
    }
```



* detail.html

```
        {% for score in scores %}
            <li>
                한줄평 : {{ score.content }} / {{ score.score }}점
            </li>
        {% endfor %}
```



### (3) 평점 삭제



* views.py - delete 함수를 만들어도 현재 있는 페이지는 detail이다

```
def comments_delete(request, movie_pk, score_pk):   # 이 부분은 받는 함수
    comment = Score.objects.get(pk=score_pk)
    
    if request.method == "POST":
        comment.delete()
    
    return redirect('movie:detail', movie_pk)
```



* urls.py

```
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.comments_delete, name="comments_delete"),
```



* detail.html

```
        {% for score in scores %}  <!--scores로 받으므로 인스턴스는 score가 된다-->
            <li>
                한줄평 : {{ score.content }} / {{ score.score }}점
                <form action="{% url 'movie:comments_delete' movie.pk score.pk %}" method="POST" onsubmit="return confirm('정말 지우시겠습니까?');" style="display:inline">
                    {% csrf_token %}
                    <input type="submit" value="평점 삭제"/>                
                </form>
            </li>
        {% endfor %}
```







* 댓글 점수 합산

```
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all()
```

| id   | content  | score | movie_id |
| ---- | -------- | ----- | -------- |
| 1    | 짱짱     | 10    | 2        |
| 2    | 고양이   | 6     | 1        |
| 3    | 마블     | 8     | 1        |
| 4    | 어벤져스 | 1     | 1        |

score 테이블의 score 컬럼(`score__score`)의 평균(Avg)을 `score_avg`라는 새로운 컬럼으로 추가적으로 붙여서 (annotate) 모든 데이터의 결과를 받아보겠다



| id   | title    | 관객수 | 포스터 | 설명   | genre_id | score_avg |
| ---- | -------- | ------ | ------ | ------ | -------- | --------- |
| 1    | 캡틴마블 | 12313  | ㅊㄷㄴ | ㅊㄷㄴ | 9        | 5         |
| 2    | ..       | ..     | ..     | ..     | ..       | ..        |
| 3    | ..       | ..     | ..     | ..     | ..       | ..        |

이렇게 score_avg가 뒤쪽 열로 붙여서 가져와진다



* views.py

```
from django.db.models import Avg    
    
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)   # score_avg 열을 왼쪽에 join해서 붙인다
```



* detail.html

```
        <p><h2>종합 평점 : {{ movie.score_avg }}</h2></p>
```



#### 참고 : django debug toolbar 설치

https://django-debug-toolbar.readthedocs.io/en/latest/ - install

```
pip install django-debug-toolbar
```



* settings.py - INSTALLED_APPS

```
    'debug_toolbar',
```



* root urls.py

```
from django.conf import settings

urlpattenrs = [
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
```



* settings.py - MIDDLEWARE

```
    'debug_toolbar.middleware.DebugToolbarMiddleware',
```



* settings.py 가장 하단부

```
STATIC_URL = '/static/'

def show_toolbar(request):
    return True
    
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}   # 이 윗 부분은 필요 없다

INTERNAL_IPS = ('0.0.0.0',)   # 집에서 할 경우(local)  127.0.0.1로 변경
```



