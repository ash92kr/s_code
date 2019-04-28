[TOC]

## fake_insta_02

**Content**

0. User
1. Signup
2. Login
3. Logout
4. User : Post = 1 : N
5. Comment
6. Like
7. People Page

> 190415-16 Mon-Tue

---

### 0. User

> [django.contrib.auth - User model](https://docs.djangoproject.com/ko/2.1/ref/contrib/auth/#user-model)

- django 에서 기본적으로 제공하는 User 모델을 그대로 사용한다.
- 반드시 `accounts` 를 사용해야 하는건 아니지만 추후에 추가적으로 설정할 코드가 줄어든다.

```bash
$ python manage.py startapp accounts
```

```python
# settings.py
INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
  ...,
] 
```

```python
# insta/urls.py
urlpatterns = [
    path('accounts/', include('accounts.urls')),
  	...
]
```

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
]
```

---

### 1. Signup

- django 에서 기본적으로 제공하는 User 모델을 사용하기 때문에 `models.py` 에 따로 작성하지 않는다.
- User 모델을 가지고 있는 `UserCreationForm` 모델폼을 사용한다.
- `is_authenticated` 으로 현재 유저가 로그인 상태인지 아닌지 확인한다.
  - 현재 회원가입시 list 페이지로 보내지만 로그인 기능을 추가하면 회원가입한 정보로 바로 로그인 되도록 할 것이다.

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
      
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

```python
# accounts/urls.py
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

```django
<!-- accounts/signup.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
		{% buttons submit="회원가입" reset="Cancel" %}{% endbuttons %}
</form>
{% endblock  %}
```

- 회원가입을 진행하고 admin 페이지 `사용자(들)`에서 확인해보자.

---

### 2. Login

> [LOGIN_URL](https://docs.djangoproject.com/ko/2.2/ref/settings/#login-url)

- 회원가입과 마찬가지로 기본 제공 모델 폼인 `AuthenticationForm` 을 사용한다.
- `login()` 함수도 기본적으로 제공하는 걸 사용하지만 view 함수와 이름이 중복되므로 `as_login` 으로 변경해서 사용한다.
- url 은 반드시 login 으로 하지 않아도 되지만 기본 redirect 경로가 `accounts/login/` 으로 설정되어 있다.
- signup.html 과 login.html 의 코드가 동일하므로 하나의 템플릿파일로 합쳐도 무관하다.

```python
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
```

```python
# accounts/urls.py
path('login/', views.login, name='login'),
```

```django
<!-- accounts/login.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
		{% buttons submit="로그인" reset="Cancel" %}{% endbuttons %}
</form>
{% endblock  %}
```

- 현재 로그인 중인 유저가 누구인지 확인하기 위해 잠시 base.html 에 다음과 같이 작성한다.
```django
<!-- base.html -->
<body>
    {% include 'posts/_nav.html' %}
    <div class="container">
        <h1>현재 유저 : {{ user.username }}</h1>
        {% block content %}
        {% endblock  %}
    </div>
```

- 회원가입 후 바로 로그인 된 상태로 만들기

```python
# accounts/views.py
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
      
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 				# 1
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

---

### 3. Logout

- 로그인과 마찬가지로 logout 함수를 가져와 사용하나 이름이 중복되므로 auth_logout 으로 변경한다.

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
```

```python
# accounts/urls.py
path('logout/', views.logout, name='logout'),
```

#### 3.1 nav 수정

- user 로그인 상태에 따라서 출력되는 링크 변경

```django
<!-- posts/_nav.html -->
<nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light px-5">
    <a class="navbar-brand" href="{% url 'posts:list' %}">
        <i class="fab fa-instagram"> | Instagram</i>
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    {% if user.is_authenticated %}
        <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <li class="nav-item">
                    <a href="{% url 'posts:create' %}" class="nav-link">New</a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">MyPage</a>
                </li>
                <li class="nav-item">
                    <a href="{% url 'accounts:logout' %}" class="nav-link">Logout</a>
                </li>
            </div>
        </div>
    {% else %}
        <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <li class="nav-item">
                    <a href="{% url 'accounts:login' %}" class="nav-link">Login</a>
                </li>
                <li class="nav-item">
                    <a href="{% url 'accounts:signup' %}" class="nav-link">Signup</a>
                </li>
            </div>
        </div>
    {% endif %}
</nav>
```

#### 3.2 login_required

> [login_required](https://docs.djangoproject.com/ko/2.2/topics/auth/default/#django.contrib.auth.decorators.login_required)

- 보이는 링크만 숨기면 주소로 바로 접근할 수 있다.

- 그래서 view 함수에서 데코레이터를 통해 막아주어야한다.

  ```python
  # posts.views.py
  from django.contrib.auth.decorators import login_required
  
  @login_required
  def create(request):
    ...
    
  @login_required
  def update(request, post_pk):
    ...
  ```

#### 3.3 next 처리

```python
# accounts/views.py
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list') # 해당 코드 수정
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
```

- 비로그인 상태로 강제로 create 와 update 페이지로 들어가보자.
- 로그인페이지로 이동되면서 url 에 붙어있는 next 주소를 확인하고 로그인해보자. next 에 붙어있는 주소로 이동되는 것을 확인 할 수 있다.

---

### 4. User : Post = 1 : N

> [Settings REF](https://docs.djangoproject.com/en/2.1/ref/settings/#settings)
>
> [Settings - AUTH_USER_MODEL](https://docs.djangoproject.com/en/2.1/ref/settings/#auth-user-model)

- 작성한 게시물(post)에 user 정보를 추가 (`user : post = 1 : N`)
- django 에서 이미 만들어 놓은 user 모델을 가져오기위해 `settings` 를 활용

```python
# posts/models.py
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
```

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to post without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1
$ python manage.py migrate
```

#### 4.1 Create 로직 수정

> [Using the Django authentication system](https://docs.djangoproject.com/ko/2.2/topics/auth/default/#using-the-django-authentication-system)

- `.save(commit=False)` 옵션은 Post 객체를 만들어서 반환하기만 하고, 실제 DB 에는 레코드를 생성하지 않는다.
- 어떤 user 의 게시글인지 보기위해 card 에 header 를 추가한다.

```python
# posts/views.py
@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)			# 1
            post.user = request.user			# 2
            post.save()				# 3
            for image in request.FILES.getlist('file'):
						...
```

```django
<!-- posts/_post.html -->
<div class="col-10 my-3">
    <div class="card">
        <div class="card-header">
            <h5 class="card-text">{{ post.user }}</h5>
        </div>
        {% if post.image_set %}
      	...
```

- 카드가 어떻게 바뀌었는지 중간 확인해보자.

#### 4.2 Authorization(Post)

- 게시글의 작성자가 post 에 기록되었기 때문에, 이제 그 작성자만 수정, 삭제가 가능하도록 해야한다.

- user 에는 현재 user(request.user) 가 저장되어있고, 해당 post.user 와 비교 후 수정버튼 출력/미출력 

  ```django
  <!-- posts/_post.html -->	
  ...      
          <div class="card-body">
              <p class="card-text">{{ post.content }}</p>
              {% if request.user == post.user %}
                  <a href="{% url 'posts:update' post.pk %}" class="btn btn-warning">수정</a>
                  <form action="{% url 'posts:delete' post.pk %}" method="post" style="display: inline;">
                      {% csrf_token %}
                      <input type="submit" value="삭제" class="btn btn-danger">
                  </form>
              {% endif %}
          </div>
      </div>
  </div>
  ```

- 버튼만 숨기면 주소로 접근이 가능하기 때문에, 실제 로직에서도 막아야한다. `post.user != request.user`

  ```python
  # posts/views.py
  @login_required
  def update(request, post_pk):
      post = get_object_or_404(Post, pk=post_pk)
      
      if post.user != request.user:
          return redirect('posts:list')
  
  def delete(request, post_pk):
      post = get_object_or_404(Post, pk=post_pk)
      
      if post.user != request.user:
          return redirect('posts:list')
  ```

---

### 5. Comment

#### 5.1 Model

- post 는 user 가 post 를 여러개 가지고 있는 1:N 이었다면, comment 는 user & post 가 여러 comment 를 가지고 있는 이중 1:N 이다
- Post, User 모델과 각각 1:N 관계 설정

```python
# posts/models.py
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
```
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

```python
# posts/forms.py
from .models import Post, Image, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
```

```python
# posts/views.py
from .forms import PostForm, ImageForm, CommentForm

def list(request):
    posts = get_list_or_404(post.objects.order_by('-pk'))
    comment_form = CommentForm()					# 1
    context = {
        'posts': posts,
        'comment_form': comment_form			# 2
    }
    return render(request, 'posts/list.html', context)
```

#### 5.2 Create

> [View decorators](https://docs.djangoproject.com/ko/2.1/topics/http/decorators/#module-django.views.decorators.http)
>
> - POST 메서드만 요청만 허용하도록 `@require_POST` 추가
> - `@require_http_methods(["GET", "POST"])` 이란 것도 있다.

```python
# posts/views.py
from django.views.decorators.http import require_POST

@login_required
@require_POST
def comment_create(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_pk
        comment.save()
    return redirect('posts:list')
```

```python
# posts/urls.py
path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
```

```django
<!-- posts/_post.html -->
                <form action="{% url 'posts:delete' post.pk %}" method="post" style="display: inline;">
                    {% csrf_token %}
                    <input type="submit" value="삭제" class="btn btn-danger">
                </form>
            {% endif %}
            <!-- 여기서부터 코드 추가 -->
            <hr>
            {% for comment in post.comment_set.all %}
                <p class="card-text"><strong>{{ comment.user }}</strong> {{ comment.content }}</p>
            {% empty %}
                <p class="card-text">댓글이 없습니다.</p>
            {% endfor %}
        </div>
        <div class="card-footer">
            <form action="{% url 'posts:comment_create' post.pk %}" method="post">
                {% csrf_token %}
                {{ comment_form }}
                <input type="submit" value="작성" class="btn-light">
            </form>
        </div>
    </div>
</div>
```

- 비로그인 유저는 댓글을 작성할 수 없게 코드 수정

  ```django
  <!-- posts/_post.html -->
          <div class="card-footer">
              {% if user.is_authenticated %}
                  <form action="{% url 'posts:comment_create' post.pk %}" method="post">
                      {% csrf_token %}
                      {{ comment_form }}
                      <input type="submit" value="작성" class="btn-light">
                  </form>
              {% else %}
                  <a href="{% url 'accounts:login' %}" class="card-link">댓글을 작성하려면 로그인하세요.</a>
              {% endif %}
          </div>
      </div>
  </div>
  ```

- 댓글 작성이 잘 되는지 확인해보자.

- 댓글 form 의 label 을 삭제해보자.

  ```python
  # posts/forms.py
  class CommentForm(forms.ModelForm):
      content = forms.CharField(label="",)
      class Meta:
          model = Comment
          fields = ['content',]
  ```

#### 5.3 Delete

- 본인이 작성한 댓글만 삭제버튼을 누를 수 있어야 한다.

```python
# posts/views.py
from .models import post, Image, Comment

@login_required
@require_POST
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')
```

```python
# posts/urls.py
path('<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
```

```django
<!-- posts/_post.html -->
{% for comment in post.comment_set.all %}
    <div class="card-text"><strong>{{ comment.user }}</strong> {{ comment.content }}
        {% if comment.user == request.user %}
            <form action="{% url 'posts:comment_delete' post.pk comment.pk %}" method="post" style="display: inline;">
                {% csrf_token %}
                <button type="submit" class="border-0"><i class="fas fa-times"></i></button>
            </form>
        {% endif %}
    </div>
{% empty %}
    <div class="card-text">댓글이 없습니다.</div>
{% endfor %}
```

---

### 6. Like

> [Many-to-many relationships](https://docs.djangoproject.com/ko/2.1/topics/db/examples/many_to_many/#many-to-many-relationships)
>
> [모델관계 다대다](https://nachwon.github.io/django-relationship/#%EB%8B%A4%EB%8C%80%EB%8B%A4-%EA%B4%80%EA%B3%84-many-to-many-relationship)
>
> [related_name](https://docs.djangoproject.com/ko/2.1/ref/models/fields/#django.db.models.ForeignKey.related_name)
>
> "user 는 여러 post 에 like 할 수 있고, post 는 여러 user 로부터 like 받을 수 있다."
>

- Like라는 것은 Post와 User 사이의 어떤 관계나 상태에 대해 정의하는 것인데, 만약에 이런 관계를 1:N이라고 가정을 하고 Post 쪽 또는 User 쪽에만 기록을 해놓는다면 특정 Post는 단 한명의 User의 좋아요만 받을 수 있게 된다거나(Post 쪽에 기록, User:Post=1:N), 반대로 특정 User는 단 하나의 Post에만 좋아요를 할 수 있게 된다(User 쪽에 기록, Post:User=1:N)

- 그래서 필요한 것이 이 두 Table 사이의 관계를 기록하는 중간 Table이고, 이 Table을 따로 생성해서 관계를 기록하는 것이 M:N 관계이다. 여기서 중간 Table을 `중개 모델(Intermediary model)`이라고 한다.

- `ManyToManyField`

  - ManyToManyField 필드 이름은 **복수형**으로 설정하는 것을 권장하고 있다.
  - 서로 관계된 모델들 중 어느 곳에 `ManyToManyField` 를 선언하든 상관이 없지만, 반드시 **한 모델**에만 선언해야하며, 의미적으로 자연스러운 관계가 되도록 선언해주는 것을 권장하고 있다.

- **관계의 역참조**

  > - **소스모델**은 `ManyToManyField` 필드가 있는 모델을 말한다. (Post)
  > - **타겟모델**은 `ManyToManyField` 에 인자로 전달되는 모델을 말한다. (User / get_user_model())
  >
  > User 모델은 Post 모델의 타겟모델이다.
  >
  > 1. 기존 1:N 관계에서는
  >
  > ```python
  > # 소스모델의 인스턴스에서 타겟모델의 인스턴스를 참조.
  > post = Post.objects.get(pk=1)
  > post.user # 1번 글을 작성한 유저를 가져온다.
  > 
  > # 역참조 - 타겟모델의 인스턴스에서 소스모델의 인스턴스를 역참조.
  > user = User.objects.get(pk=1)
  > user.post_set.all() # 소스모델의 이름은 Post 이므로, 역참조 매니저의 이름은 post_set 이 된다.
  > ```
  >
  > 2. 그런데 M:N 관계가 되면
  >
  > ```python
  > post = Post.objects.get(pk=1)
  > post.user
  > post.like_users
  > 
  > user = User.objects.get(pk=1)
  > user.post_set.all() # 역참조시에 문제 발생
  > # 내가 작성한 글들 vs 내가 좋아요한 글들 인지 알수가 없다.
  > # 그래서 user 쪽에서 좋아요한 post 들을 불러올 related_name 설정이 필요하다.
  > 
  > # related_name 을 like_posts 로 설정했다면,
  > user.like_posts.all() # 은 내가 좋아요한 글들을 참조할 수 있다.
  > ```

```python
# posts/models.py
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    content = models.TextField()
    # blank=True 가 없다면 글을 작성할때마다 좋아요 값이 필요하기 때문에 글이 작성되지 않는다.

    def __str__(self):
        return self.content
```
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> `posts_post_like_users` 라는 테이블이 만들어진다.
>
> - 두 테이블 간의 M:N 관계를 나타내주는 **중개 모델(Intermediary model)**이다.
>
> |  id  | post_id | user_id |
> | :--: | :-----: | :-----: |
> |  .   |    .    |    .    |

```python
# posts/views.py

# 1
@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:list')


# 2
@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
		user = request.user
    # 이미 해당 유저가 like 를 누른 상태면 좋아요 취소(해당 유저가 like_users 컬럼에 존재하면 해당 유저를 지움)
    if post.like_users.filter(pk=user.pk).exists():
        post.like_users.remove(user)
    # 안 눌렀다면 좋아요
    else:
        post.like_users.add(user)
    return redirect('posts:list')
```

```python
# posts/urls.py
path('<int:post_pk>/like/', views.like, name='like'),
```

- `posts/_post.html`

  ```django
          <div class="card-body">
              <a href="{% url 'posts:like' post.pk %}" class="card-link">
                  {% if user in post.like_users.all %}
                      <i class="fas fa-heart fa-lg" style="color:crimson"></i>
                  {% else %}
                      <i class="far fa-heart fa-lg" style="color:black"></i>
                  {% endif %}
              </a>
              <p class="card-text">{{ post.like_users.count }} 명이 좋아합니다.</p>
              <p class="card-text">{{ post.content }}</p>
  ```

---

### 7. People Page

- 지금 만드는 페이지는 User 의 CRUD 중 R, 구체적으로는 Detail 페이지에 해당한다.

  ```python
  # accounts/views.py
  from django.shortcut import render, redirect, get_object_or_404
  from django.contrib.auth import get_user_model
  
  def people(request, username):
      people = get_object_or_404(get_user_model(), username=username)
      context = {'people': people,}
      return render(request, 'accounts/people.html', context)
  ```

- 인스타 주소 구조와 비슷하게 만들기 위해 `insta/urls.py` 에 주소를 작성해본다.

  > 어떤 앱의 view 인지 구분하기 위해 `as` 로 이름을 바꿔준다.
  >
  > **이 주소는 반드시 가장 최하단에 작성해야 한다. django 는 url 또한 위에서부터 읽어내려오기 때문**

  ```python
  # insta/urls.py
  from accounts import views as accounts_views
  
  urlpatterns = [
  		...
      path('<str:username>/', accounts_views.people, name='people'),
  ]
  ```

- 이제 프로필 페이지를 만들어보자

  > 구현 목록
  >
  > 1. 내가 작성한 글 목록(bootstrap Card & Carousel)
  >    - 업로드한 사진의 가장 첫번재 사진이 보이도록 한다. `post.image_set.first.file.url`
  >    - 최근에 작성한 글이 가장 먼저 오도록 정렬한다. `dictsortreversed:"pk"`
  >    - 게시글에 좋아요 누른 유저 수. `post.like_users.count`
  >    - 게시글에 달린 댓글 수. `post.comment_set.count`
  > 2. 내가 작성한 댓글 목록 (bootstrap Card Quote)
  >    - 최근에 작성한 댓글이 가장 먼저 오도록 정렬한다.

  ```django
  <!-- accounts/people.html -->
  {% extends 'base.html' %}
  {% block content %}
  <h1 class="text-center">{{ people.username }}'s Profile</h1>
  <h3 class="text-center">내가 작성한 글</h3>
  <div class="row">
      {% for post in people.post_set.all|dictsortreversed:"pk" %}
      <div class="col-4 my-2">
          <div class="card">
              <img src="{{ post.image_set.first.file.url }}" class="d-block w-100" alt="{{ post.image_set.first.file }}">
              <div class="card-body">
                  <h5 class="card-title">{{ post.content }}</h5>
                  <p class="card-text">{{ post.like_users.count }} 명이 좋아합니다.</p>
                  <p class="card-text">{{ post.comment_set.count }} 개의 댓글.</p>
                  <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
          </div>
      </div>
      {% endfor %}
  </div>
  <hr>
  <hr>
  <h3 class="text-center">내가 작성한 댓글</h3>
  <div class="row">
      {% for comment in people.comment_set.all|dictsortreversed:"pk" %}
      <div class="col-12 my-2">
          <div class="card">
              <div class="card-body">
                  <blockquote class="blockquote">
                      <p class="mb-0">{{ comment.post }}</p>
                      <footer class="blockquote-footer">{{ comment }}</footer>
                  </blockquote>
              </div>
          </div>
      </div>
      {% endfor %}
  </div>
  {% endblock %}
  ```

- 프로필 페이지에 맞춰 nav 와 base 템플릿을 수정해보자.

- `_nav.html` 수정

  > ```django
  > <!-- 해당 코드 추가 -->
  > <div></div>
  > <div class="navbar-nav">
  >  <li class="nav-item">
  >      <span class="navbar-text">{{ user.username }} 님 반갑습니다.</span>
  >  </li>
  > </div>
  > ```
  >
  > - `justify-content-end` 를 `justify-content-between` 로 변경
  > - navbar 테마 dark 로 변경 : `navbar-dark bg-dark`
  > - `text-light` 반갑습니다 글자 하얗게 출력

  ```django
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark px-5">
  		...
      {% if user.is_authenticated %}
      <div class="collapse navbar-collapse justify-content-between" id="navbarNavAltMarkup">
          <div></div>
          <div class="navbar-nav">
              <li class="nav-item">
                  <span class="navbar-text text-light">{{ user.username }} 님 반갑습니다.</span>
              </li>
          </div>
          <div class="navbar-nav">
              <li class="nav-item">
                  <a href="{% url 'posts:create' %}" class="nav-link">New</a>
              </li>
              <li class="nav-item">
                  <a href="{% url 'people' user.username %}" class="nav-link">MyPage</a>
              </li>
              <li class="nav-item">
                  <a href="{% url 'accounts:logout' %}" class="nav-link">Logout</a>
              </li>
          </div>
      </div>
      {% else %}
  		...
  </nav>
  ```

- `base.html` 변경

  > `<h1>현재 유저 : {{ user.username }}</h1>` 삭제

  ```django
  <!-- base.html -->
  <body>
      {% include 'posts/_nav.html' %}
      <div class="container">
          {% block content %}
          {% endblock  %}
      </div>
  ```

---

```
insta_project
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── accounts
│   │       ├── login.html
│   │       ├── people.html
│   │       └── signup.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── insta
│   ├── settings.py
│   ├── templates
│   │   └── base.html
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── posts
│   │   └── images
│   │       ├── sample_img_QEOEpX0.jpg
│   │       ├── sample_img_ryBnDMs.jpg
│   │       └── sample_img_sVRSSZ8.jpg
│   └── sample_img_2.jpg
└── posts
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_post_image.py
    │   ├── 0003_auto_20190412_0246.py
    │   ├── 0004_auto_20190412_0256.py
    │   ├── 0005_post_user.py
    │   ├── 0006_comment.py
    │   ├── 0007_post_like_users.py
    ├── models.py
    ├── templates
    │   └── posts
    │       ├── _nav.html
    │       ├── _post.html
    │       ├── form.html
    │       └── list.html
    ├── tests.py
    ├── urls.py
    └── views.py
```
