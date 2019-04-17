[TOC]

## Fake_Insta_01

**Content**

0. 시작하기
1. 모델 정의
2. 공용 템플릿
3. CRUD with ModelForm
4. Upload Image
5. Upload Multiple Images
6. favicon

> 190411 & 12 | Thu~Fri

---

> **1. django 2.2 버전이 2019.04.01 부로 정식 릴리즈 되었습니다.** [Django 2.2 released](https://www.djangoproject.com/weblog/2019/apr/01/django-22-released/)
>
> - 따라서 앞으로 django 설치 시 버전을 명시해주어야 합니다.
>
> ```bash
> $ pip install django==2.1.8
> ```
>
> - 2.2 버전은 sqlite 버전 3.8.3 이상을 사용하도록 되어있는데, c9에 기본 설치된 sqlite 버전은 3.8.2 라서 sqlite 버전을 올리지 않으면 에러가 발생합니다.
>
> - 원한다면, Django 2.2 + sqlite 3.8.3 이상 조합으로 사용해도 되지만 다른 어떤 오류들이 발생하는지 아직 테스트 되지 않았습니다.
>
> **2. C9 서비스 종료 이슈**
>
> - 2019년 6월 30일까지만 워크스페이스 생성 + 사용가능. 12월 31일 완전 종료.

---

### 0. 시작하기

  ```shell
$ mkdir insta_project
$ cd insta_project

$ pyenv virualenv 3.6.7 insta-venv
$ pyenv local insta-venv

$ pip install django==2.1.8

$ django-admin startproject insta .
$ python manage.py startapp posts
  ```

  ```python
# settings.py
INSTALLED_APPS = [
  'posts.apps.PostsConfig',
]

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_TZ = False
  ```

  ```python
# insta/urls.py
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
  ```

```python
# posts/urls.py
from django.urls import path

app_name = 'posts'
urlpatterns = [
    
]
```

---

### 1. 모델 정의

- 처음은 간단하게 하나의 컬럼만 있는 모델을 만들고, 나중에 기능을 붙이면서 하나씩 추가해 나간다.

```python
# posts/models.py
class Post(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- admin 설정

  ```bash
  $ python manage.py createsuperuser
  ```

  ```python
  # admin.py
  from .models import Post
  
  class PostAdmin(admin.ModelAdmin):
      list_display = ['content',]
  admin.site.register(Post, PostAdmin)
  ```

- admin 페이지에서 게시글 하나 작성해보기

---

### 2. 공용 템플릿 

- 공용 템플릿을 프로젝트 insta 폴더 안에 `templates` 폴더에 추가할 것이다.

  ```python
  # settings.py
  TEMPLATES = [
      {
          ...,
          'DIRS': [os.path.join(BASE_DIR, 'insta', 'templates')],
  				...
  ```

- 이제 `base.html` 을 작성한다.

  ```django
  <!-- templates/base.html -->
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
      <title>INSTA</title>
  </head>
    
  <body>
      <div class="container">
          {% block content %}
          {% endblock  %}
      </div>
    
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  > 인스타그램처럼 만들 예정이기 때문에 bootstrap 과 fontawsome CDN 을 추가한다.

#### 2.1 템플릿 분할

- nav 나 반복되는 특정 구역을 모두 base.html 에 한 곳에 작성하는 것 보다는, 구역 별로 템플릿을 만들어서 필요한 위치에 가져오는 것이 코드 유지보수에 유용하다. (모듈화)

- 분할된 템플릿의 파일명은 `_nav.html` 처럼 언더바(`_`)로 시작하는 것이 관례다.

- fontawesome 에서 아이콘도 가져와서 넣는다.

  ```django
  <!-- templates/posts/_nav.html -->
  <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light px-5">
      <a class="navbar-brand" href="#">
          <i class="fab fa-instagram"> | Instagram</i>
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
          <div class="navbar-nav">
              <li class="nav-item">
                  <a href="#" class="nav-link">New</a>
              </li>
              <li class="nav-item">
                  <a href="#" class="nav-link">MyPage</a>
              </li>
          </div>
      </div>
  </nav>
  ```

- `{% include %}` 로 분할된 템플릿을 가져올 수 있다.

  ```django
  <!-- templates/base.html -->
  <body>
      {% include 'posts/_nav.html' %}
      <div class="container">
          {% block content %}
          {% endblock  %}
      </div>
  ```

---

### 3. CRUD with ModelForm

#### 3.1 Create

```python
# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]
```

```python
# posts/views.py
from django.shortcuts import render, redirect
from .forms import PostForm

def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
          	post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    context = {'post_form': post_form,}
    return render(request, 'posts/form.html', context)
```

```python
# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('create/', views.create, name='create'),
]
```

```django
<!-- posts/form.html -->
{% extends "base.html" %}
{% load bootstrap4 %}

{% block content %}
<h1>NEW</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ post_form }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
{% endblock  %}
```

##### 3.1.1 django-bootstrap4

> [django-bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/installation.html)

- 밋밋한 form 을 꾸며주기 위해 bootstrap 을 사용할 것이다.
- form class 에 bootstrap 을 적용시켜주는 외부라이브러리 `django-bootstrap4` 를 설치해서 사용한다.

```bash
$ pip install django-bootstrap4
```

```python
# settings.py
INSTALLED_APPS = [
    'bootstrap4',
  	...
```

```django
<!-- posts/form.html -->
{% extends "base.html" %}
{% load bootstrap4 %}

{% block content %}
<h1>NEW</h1>
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form post_form %}
    {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
  	<a href="{% url 'posts:list' %}" class="btn btn-info">Back</a>
</form>
{% endblock  %}
```

- create 페이지를 확인해보자.

#### 3.2 Read

> Class Based View 를 조금씩 준비하기 위해 이제 index 가 아닌 list 로 명명해보자.

```python
# posts/views.py
from django.shortcuts import render, redirect, get_list_or_404
from .models import Post

def list(request):
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)
```

```python
# posts/urls.py
path('', views.list, name='list'),
```

```django
<!--- posts/list.html -->
{% extends 'base.html' %}
{% block content %}
<h1>LIST</h1>
{% for post in posts %}
    {% include 'posts/_post.html' %}
{% endfor %}
{% endblock  %}
```

- 게시물 하나를 표시하는 템플릿을 `_post.html` 로 분할한다.

  - 추후에 재사용을 위해! (전체 글을 보여주는 페이지, 해시태그를 포함하는 게시물끼리 보여줄 때, user page 등)

  ```django
  <!--- posts/_post.html -->
  <div class="card" style="width: 18rem;">
      <img src="#" class="card-img-top" alt="#">
      <div class="card-body">
          <p class="card-text">{{ post.content }}</p>
      </div>
  </div>
  ```

#### 3.3 Update

- ModelForm 을 사용하기 때문에 로직이 간단하다.
- create 가 사용하는 form.html 을 함께 사용한다.

```python
# posts/views.py
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form,}
    return render(request, 'posts/form.html', context)
```

```python
# posts/urls.py
path('<int:post_pk>/update/', views.update, name='update'),
```

```django
<!-- posts/form.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
{% if request.resolver_match.url_name == 'create' %}
    <h1>NEW</h1>
{% else %}
    <h1>EDIT</h1>
{% endif %}
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form post_form %}
    {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
  	<a href="{% url 'posts:list' %}" class="btn btn-info">Back</a>
</form>
{% endblock  %}
```

```django
<!--- posts/_post.html -->
<div class="card my-3">
  <img src="#" class="card-img-top" alt="#">
  <div class="card-body">
    <p class="card-text">{{ post.content }}</p>
    <a href="{% url 'posts:update' post.pk %}" class="btn btn-warning">수정</a>
  </div>
</div>
```

#### 3.5 Delete

```python
# posts/views.py
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')
```

```python
# posts/urls.py
path('<int:post_pk>/delete/', views.delete, name='delete'),
```

```django
<!-- posts/_post.html -->
<div class="card my-3">
	<img src="#" class="card-img-top" alt="#">
  <div class="card-body">
    <p class="card-text">{{ post.content }}</p>
    <a href="{% url 'posts:update' post.pk %}" class="btn btn-warning">수정</a>
    <form action="{% url 'posts:delete' post.pk %}" method="POST" style="display: inline;">
        {% csrf_token %}
        <input type="submit" value="삭제" class="btn btn-danger">
    </form>
  </div>
</div>
```

---

### 4. Upload Image

> [Django_07 수업자료 참고](https://github.com/djpy2/Django/blob/master/Django_07.md#django_07)

#### 4.1 Model

```python
# models.py
class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.content
```

```bash
$ pip install Pillow
$ python manage.py makemigrations
$ python manage.py migrate
```

- PostForm 에 방금 만든 image 컬럼(필드)를 추가한다.

  ```python
  # posts/forms.py
  class PostForm(forms.ModelForm):
      class Meta:
          model = Post
          fields = ['content', 'image',]
  ```

- 넘어온 이미지 파일은 request.POST 가 아닌 `request.FILES` 에 들어있으므로 PostForm 에 새로 추가한다.

  ```python
  # posts/views.py
  def create(request):
      if request.method == 'POST':
          post_form = PostForm(request.POST, request.FILES)
          if post_form.is_valid():
            	post_form.save()
              return redirect('posts:list')
      else:
          post_form = PostForm()
      context = {'post_form': post_form,}
      return render(request, 'posts/form.html', context)
  ```

- 파일 업로드를 위해 form tag 속성 `enctype="multipart/form-data"` 추가

  - `accept="image/*"` 은 ModelForm 을 사용하면 input 에 자동으로 설정되어 있기 때문에 작성하지 않아도 된다.

  ```django
  <!-- posts/form.html -->
  <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {% bootstrap_form post_form %}
      {% buttons submit="Submit" reset="Cancel" %}{% endbuttons %}
    	<a href="{% url 'posts:list' %}" class="btn btn-info">Back</a>
  </form>
  ```

> 이 상태로 이미지를 업로드하면 이미지 파일이 엉뚱한 곳으로 올라간다. (BASE_DIR)

- New Post Link

  - _nav.html 에 새 글을 작성하는 페이지로 이동하는 링크를 만든다.

  ```django
  <!-- posts/_nav.html -->
  <li class="nav-item">
    <a href="{% url 'posts:create' %}" class="nav-link">New</a>
  </li>
  ```

#### 4.2 Media

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```python
# insta/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 사진이 없는 게시물의 경우 에러가 발생하기 때문에 분기 처리한다.

  ```django
  <!--- posts/_post.html -->
  <div class="card my-3">
    {% if post.image %}
    	<img src="{{ post.image.url }}" class="card-img-top" alt="{{ post.image }}">
    {% else %}
    	<img src="#" class="card-img-top" alt="No_image">
    {% endif %}
    <div class="card-body">
      <p class="card-text">{{ post.content }}</p>
      <a class="btn btn-warning" href="{% url 'posts:update' post.pk %}">수정</a>
      <form action="{% url 'posts:delete' post.pk %}" method="POST" style="display: inline;">
        {% csrf_token %}
        <input type="submit" class="btn btn-danger" value="삭제">
      </form>
    </div>
  </div>
  ```

- 이미지를 포함한 새로운 게시글 작성해보기.

#### 4.3 Image Resizing

- 인스타의 경우 600*600 의 이미지 사이즈를 갖는다.

- 필요 패키지 사전 설치

  ```bash
  $ pip install pilkit
  $ pip install django-imagekit
  ```

```python
# settings.py
INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    'bootstrap4',
    'imagekit',
		...
]
```

```python
# posts/models.py
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    content = models.TextField()
    image = ProcessedImageField(
        upload_to='posts/images',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 90},
    )

    def __str__(self):
        return self.content
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> 업로드 테스트 진행.

---

### 5. Upload Multiple Images

#### 5.1 Model

- 여러 장의 이미지를 업로드하기 위해 Image 모델을 새로 만들고 Post 모델과 1:N 관계를 설정한다.

  ```python
  # posts/models.py
  class Post(models.Model):
      content = models.CharField(max_length=140)
  
      def __str__(self):
          return self.content
  
  class Image(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE)
      file = ProcessedImageField(
              upload_to='posts/images',				
              processors=[ResizeToFill(600, 600)],	
              format='JPEG',											
              options={'quality': 90},						
          )
  ```

  ```python
  # posts/forms.py
  class PostForm(forms.ModelForm):
      class Meta:
          model = Post
          fields = ['content',] # image 필드 삭제
  ```

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

#### 5.2 ModelForm

- ImageForm 에서 여러 장 업로드를 위해 widgets 에 `multiple` 옵션을 설정한다.

  ```python
  # posts/forms.py
  from .models import Post, Image
  
  class ImageForm(forms.ModelForm):
      class Meta:
          model = Image
          fields = ['file',]
          widgets = {
              'file': forms.FileInput(attrs={'multiple': True}),
          }
  ```

- 이미지 파일이 아닌 경우 업로드 되지 않도록 한다.

  - form 변수이름 중복을 피하기 위해 `board_form`, `image_form` 으로 변경한다.
  - **`ModelForm(data=request.POST, files=request.FILES)` 처럼 키워드 인자로 넘길 수 있다.**

  ```python
  # posts/views.py
  from .forms import PostForm, ImageForm
  from .models import Post, Image
  
  def create(request):
      if request.method == 'POST':
          post_form = PostForm(request.POST)
          if post_form.is_valid():
              post = post_form.save()
              for image in request.FILES.getlist('file'):
                  request.FILES['file'] = image
                  image_form = ImageForm(files=request.FILES)
                  if image_form.is_valid():
                      image = image_form.save(commit=False)
                      image.post = post
                      image.save()
              return redirect('posts:list')
      else:
          post_form = PostForm()
          image_form = ImageForm()
      context = {
          'post_form': post_form,
          'image_form': image_form,
          }
      return render(request, 'posts/form.html', context)
  ```

- bootstrap carousel 을 통해 여러장 보여주기

  ```django
  <!-- posts/_post.html -->
  <div class="card">
      {% if post.image_set %}
          <div id="post{{post.pk}}" class="carousel slide carousel-fade" data-ride="carousel">
              <div class="carousel-inner">
                  {% for image in post.image_set.all %}
                      <div class="carousel-item {% if forloop.counter == 1 %} active {% endif %}">
                          <img src="{{ image.file.url }}" class="d-block w-100" alt="{{ image.file }}">
                      </div>
                  {% endfor %}
              </div>
              <a class="carousel-control-prev" href="#post{{post.pk}}" role="button" data-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="sr-only">Previous</span>
              </a>
              <a class="carousel-control-next" href="#post{{post.pk}}" role="button" data-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="sr-only">Next</span>
              </a>
          </div>
      {% else %}
          <img src="#" alt="no_image">
      {% endif %}
      <div class="card-body">
  ```

- 인스타는 기존 게시글 이미지를 수정하지 못하므로 update 로직은 그대로 유지하지만 수정 페이지에서는 image form 이 보이지 않도록 분기한다.

  ```django
  <!-- posts/form.html -->
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  
  {% block content %}
  		...
  <form action="" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {% bootstrap_form post_form %}
      {% if image_form %}
          {% bootstrap_form image_form show_label=False %}
      {% endif %}
      ...
  ```

- 인스타처럼 보이기 위한 다듬기

  ```django
  <!-- posts/list.html -->
  {% extends 'base.html' %}
  {% block content %}
  <h1>LIST</h1>
  <div class="d-flex flex-wrap justify-content-center">
      {% for post in posts %}
          {% include 'posts/_post.html' %}
      {% endfor %}
  </div>
  {% endblock  %}
  ```

  ```django
  <!-- posts/_post.html -->
  <div class="col-10 my-3">
    <div class="card">
  		...
    </div>
  </div>
  ```

  - instagram 이미지 nav 링크 설정하기

  ```django
  <!-- posts/_nav.html -->
  <nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light px-5">
      <a class="navbar-brand" href="{% url 'posts:list' %}">
          <i class="fab fa-instagram"> | Instagram</i>
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
          <div class="navbar-nav">
              <li class="nav-item">
                  <a href="{% url 'posts:create' %}" class="nav-link">New</a>
              </li>
              <li class="nav-item">
                  <a href="#" class="nav-link">MyPage</a>
              </li>
          </div>
      </div>
  </nav>
  ```

---

### 6. favicon

> [Managing static files](https://docs.djangoproject.com/en/2.2/howto/static-files/#managing-static-files-e-g-images-javascript-css)

- static 의 기본 경로는 `[APP_NAME]/static` 이다.
- `posts/static/posts/` 에 favicon 파일을 넣는다.

```django
<!-- base.html -->
{% load static %}
...
<link rel="shortcut icon" type="image/png" href="{% static 'posts/instagram.png' %}">
```

---

```
insta_project
├── db.sqlite3
├── insta
│   ├── settings.py
│   ├── templates
│   │   └── base.html
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── IMG_4228.JPG
│   └── posts
│       └── images
│           ├── IMG_4228.JPG
│           ├── sample_img.jpg
│           ├── sample_img_JxYansA.jpg
│           ├── sample_img_KyFo2ol.jpg
│           ├── ssafy-1210-01.jpg
│           ├── ssafy-1210-01_PGBQHo9.jpg
│           └── ssafy-1210-01_zKUhFgW.jpg
├── posts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_post_image.py
│   │   ├── 0003_auto_20190412_1436.py
│   │   ├── 0004_auto_20190412_1441.py
│   ├── models.py
│   ├── static
│   │   └── posts
│   │       └── instagram.png
│   ├── templates
│   │   └── posts
│   │       ├── _nav.html
│   │       ├── _post.html
│   │       ├── form.html
│   │       └── list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
```

