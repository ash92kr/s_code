[TOC]

## Django_11

**Content**

0. Comment
1. Profile
2. 매끄럽게

> 190410 & 11 /  Wed~Thu

---

### 0. Comment

#### 0.1 Model

- Comment 모델은 Board, User 모델과 각각 1:N 관계를 이룬다.

  ```python
  # boards/models.py
  class Comment(models.Model):
      board = models.ForeignKey(Board, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      content = models.CharField(max_length=140)
      
      def __str__(self):
          return self.content
  ```

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  ```python
  # boards/forms.py
  from .models import Board, Comment
  
  class CommentForm(forms.ModelForm):
      class Meta:
          model = Comment
          fields = ['content',]
  ```

#### 0.2 Create

> [View decorators](https://docs.djangoproject.com/ko/2.1/topics/http/decorators/#module-django.views.decorators.http)

```python
# boards/views.py
from django.views.decorators.http import require_POST
from .forms import BoardForm, CommentForm

def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comment_form = CommentForm()
    context = {
        'board': board,
        'comment_form': comment_form,
        }
    return render(request, 'boards/detail.html', context)
  
@require_POST
def comment_create(request, board_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
      # comment 를 바로 저장하지 않고 현재 user, board_pk 정보를 넣어서 저장
        comment = form.save(commit=False)
        comment.user = request.user
        comment.board_id = board_pk
        comment.save()
    return redirect('boards:detail', board_pk)
```

```python
path('<int:board_pk>/comments/', views.comment_create, name='comment_create'),
```

```django
<!-- boards/detail.html -->
{% load crispy_forms_tags %}
<p>{{ board.content }}</p>
<hr>
{% for comment in board.comment_set.all %}
    <div><b>{{ comment.user }}</b> : {{ comment.content }}<div>
{% empty %}
    <div>댓글이 없습니다.</div>
{% endfor %}
<hr>
<form action="{% url 'boards:comment_create' board.pk %}" method="post">
  {% csrf_token %}
  {{ comment_form | crispy }}
  <input type="submit" value="작성">
</form>
```

- 비로그인 유저는 댓글을 작성할 수 없도록 코드 수정 (+ `@login_required`)

  ```django
  <!-- boards/detail.html -->
  {% if user.is_authenticated %}
      <form action="{% url 'boards:comment_create' board.pk %}" method="post">
          {% csrf_token %}
          {{ comment_form | crispy }}
          <input type="submit" value="작성">
      </form>
  {% else %}
      <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인하세요.</a>
  {% endif %}
  ```

#### 0.3 Delete

- 현재 user 와 댓글의 user 가 같다면 삭제버튼을 누를 수 있고, 아니라면 삭제버튼을 출력하지 않도록 if 문 추가

  ```django
  {% if user == comment.user %}
  	...
  {% endif %}
  ```

```python
# boards/views.py
from .models import Board, Comment

@require_POST
@login_required
def comment_delete(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('boards:detail', board_pk)
```

```python
path('<int:board_pk>/comments/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
```

```django
<!-- boards/detail.html -->
{% for comment in board.comment_set.all %}
    <div>
    <b>{{ comment.user }}</b> : {{ comment.content }}
    {% if user == comment.user %}
        <form action="{% url 'boards:comment_delete' board.pk comment.pk %}" method="post" style="display: inline;">
            {% csrf_token %}
            <input type="submit" value="삭제">
        </form>
    {% endif %}
    </div>
{% empty %}
    <p>댓글이 없습니다.</p>
{% endfor %}
<hr>
...
```

---

### 1. Profile

- user 한명의 profile 페이지를 인스타와 비슷하게 만들 것이다.

- 프로필 페이지에는 user 가 작성한 board 와 comment 들을 보여준다.

  ```python
  # accounts/views.py
  from django.shortcuts import get_object_or_404
  from django.contrib.auth import get_user_model
  
  def profile(request, user_pk):
      user_info = get_object_or_404(get_user_model(), pk=user_pk)
      context = {
          'user_info': user_info,
      }
      return render(request, 'accounts/profile.html', context)
  ```

  ```python
  # accounts/urls.py
  path('profile/<int:user_pk>/', views.profile, name='profile'),
  ```

- 프로필 유저가 쓴 글 출력

  ```django
  <!-- accounts/profile.html -->
  {% extends 'boards/base.html' %}
  {% block body %}
  {% load crispy_forms_tags %}
  
  <h2>{{ user_info.username }}'s Profile</h2>
  <h3>{{ user_info.username }}'s Boards</h3>
  {% for board in user_info.board_set.all %}
      제목 : <a href="{% url 'boards:detail' board.pk %}">{{ board.title }}</a><br>
      내용 : {{ board.content }}<br>
      달린 댓글 수 : {{ board.comment_set.all.count }}<br>
      <hr>
  {% endfor %}
  {% endblock %}
  ```

- 프로필 유저가 쓴 댓글 출력

  ```django
  <!-- accounts/profile.html -->
  <hr>
  <h3>{{ user_info.username }}'s Comments</h3>
  {% for comment in user_info.comment_set.all %}
      <div>{{ comment }}</div>
  {% endfor %}
  {% endblock %}
  ```

  - 댓글이 달린 게시글의 제목과 링크 연결

     ```django
    <!-- accounts/profile.html -->
    {% for comment in user_info.comment_set.all %}
        <div>{{ comment }} - <a href="{% url 'boards:detail' comment.board_id %}">[게시글 제목 : {{comment.board}}]</a></div>
    {% endfor %}
    ```

- `index.html` 에서 작성자를 클릭하면 작성자의 profile 로 이동하도록 수정

  ```django
  <!-- boards/index.html -->
  {% for board in boards %}
      <p><b>작성자 : <a href="{% url 'accounts:profile' board.user_id %}">{{ board.user }}</a></b></p>
      <p>{{ board.pk }}</p>
      <p>{{ board.title }}</p>
      <a href="{% url 'boards:detail' board.pk %}">글 보러가기</a>
      <hr>
  {% endfor %}
  ```

---

### 2. 매끄럽게

- 프로필용 `accounts/base.html` 만들기

  ```django
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <title>Profile</title>
  </head>
  <body>
      <div class="container">
          {% block body %}
          {% endblock %}
      </div>
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

- `boards/base.html` 정리

  - gravatar 삭제
  - nav 링크
    - gravatar 삭제
    - 로그인시  : 내 프로필 / 로그아웃
    - 비로그인시 : 로그인 / 회원가입

  ```django
  <!-- boards/base.html -->
  <body>
      <div class="container">
      {% if user.is_authenticated %}
          <h1>
              안녕, {{ user.username }}
              <a href="{% url 'accounts:profile' user.pk %}">[내 프로필]</a>
              <a href="{% url 'accounts:logout' %}">[로그아웃]</a>
          </h1>
      {% else %}
          <h1>
              <a href="{% url 'accounts:login' %}">로그인</a>
              <a href="{% url 'accounts:signup' %}">회원가입</a>
          </h1>
      {% endif %}
  ```

- `accounts/base.html` 작성

  - nav 링크
    - 로그인시 : 로그아웃
    - 비로그인시 : 로그인 / 회원가입

  ```django
  <!-- accounts/base.html -->
  <body>
      <div class="container">
      {% if user.is_authenticated %}
          <h1>
              <a href="{% url 'accounts:logout' %}">[로그아웃]</a>
          </h1>
      {% else %}
          <h1>
              <a href="{% url 'accounts:login' %}">로그인</a>
              <a href="{% url 'accounts:signup' %}">회원가입</a>
          </h1>
      {% endif %}
      <hr>
          {% block body %}
          {% endblock %}
      </div>
  ```

- `accounts/profile.html` 추가 작성

  - 현재 유저와 프로필 유저가 일치(`user == user_info`)하면 `내정보수정`,`비밀번호 변경`, `탈퇴` 링크 보이기
  - gravatar `{{ user.email }}` 이 아닌 `{{ user_info.email }}` 로 변경

  ```django
  <!-- accounts/profile.html -->
  {% extends 'accounts/base.html' %}
  {% block body %}
  {% load gravatar %}
  
  <h2><img src="https://s.gravatar.com/avatar/{{ user_info.email|makemd5 }}?s=80" alt="gravatar">{{ user_info.username }}'s Profile</h2>
  {% if user == user_info %}
      <a href="{% url 'accounts:edit' %}">[내정보 수정]</a>
      <a href="{% url 'accounts:change_password' %}">[비밀번호 변경]</a>
      <form action="{% url 'accounts:delete' %}" method="post" style="display: inline;" onsubmit="return confirm('R U SURE?');">
          {% csrf_token %}
          <input type="submit" value="탈퇴">
      </form>
  {% endif %}
  <hr>
  ...
  ```

- 기본적인 로직과 구조가 맞추어 졌으니 부트스트랩을 통해 최대한 인스타 프로필 처럼 만들어보자 !