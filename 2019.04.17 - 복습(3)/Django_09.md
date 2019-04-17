[TOC]

## Django_09

**Content**

0. Authentication
1. Sign up
2. Login
3. Logout
4. 매끄럽게
5. 회원 탈퇴
6. 회원 수정
7. 비밀번호 변경
8. Authorization
9. auth_form 합치기
10. User - Board

> 190408 & 09 Mon~Tue

---

### 0. Authentication(인증)

> [Using the Django authentication system](https://docs.djangoproject.com/en/2.1/topics/auth/default/#using-the-django-authentication-system)

- 이전 ModelForm 수업에 이어서 진행한다.
- django 에는 기본적으로 로그인 기능이 구현되어 있다.
  - createsuperuser 로 계정을 만들고, admin 페이지에서 로그인을 할 수 있었던 이유.
- 기능 자체는 구현이 되어 있으므로 우리는 로그인 페이지만 만들면 된다.
  - 하지만, `게시글 작성` 과는 다른 `로그인` 이라는 새로운 기능을 만드므로 새 app인 `accounts` 을 만든다.

```bash
$ python manage.py startapp accounts
```

```python
# settings.py
INSTALLED_APPS = [
    'boards.apps.BoardsConfig',
    'accounts.apps.AccountsConfig',
```

```python
# myform/urls.py
path('accounts/', include('accounts.urls')),
```

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
]
```

> app 이름이 반드시 accounts 일 필요는 없으나, 후에 auth 관련된 기본 값들이 accounts 로 되어 있는 모습을 발견하게 될 것이다. 되도록 accounts 라는 이름을 사용한다.

---

### 1. Sign up

> [Using the Django authentication system - Built-in forms](https://docs.djangoproject.com/ko/2.2/topics/auth/default/#module-django.contrib.auth.forms)

- 회원가입은 CRUD 로직에서 User 를 Create 하는 것과 같다.
- `class User` Model 은 django 가 미리 만들어 놨다.
- 그리고 이 User 모델과 연동된 ModelForm 인 `UserCreationForm` 도 만들어져 있다.

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

```python
# accounts/urls.py
path('signup/', views.signup, name='signup')
```

```django
<!-- accounts/signup.html -->
{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}

<h1>회원 가입</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ form|crispy }}
    <input type="submit" value="Submit"/>
</form>
{% endblock %}
```

> admin 페이지에서 새로운 user 가 생겼는지 확인, User Model 은 admin 페이지에 이미 등록도 되어 있다.

---

### 2. Login

- 새로운 user 를 만들었으니, 만든 user 정보로 로그인을 해보자.
- 로그인도 Create 로직과 같지만 Session 을 Create 하는 것이다.
  - Session 이란 브라우저의 정보를 가져와 임시로 들고 있도록해서, 지금 이 페이지를 보는게 누구인지 구분하도록 서버 쪽에서 정보를 들고 있는 것을 의미한다. (간단 설명)
  - 그래서 이 session 은 사용자가 로그인 하면, 로그인한 사용자의 정보를 페이지가 전환되더라도 계속 들고 있는다. (로그아웃 버튼을 누르거나, sesstion 만료시간이 지날 때 까지 들고 있는다.)
- Session 은 잠시 뒤로 넘기고 우리는 django 가 세션 관리를 알아서 모두 해준다는 것을 알고 가자.
- User 를 만드는 ModelForm 은 `AuthenticationForm` 을 사용한다.
  - `auto_login` 은 session 에 user 정보를 기록해서 계속 들고 있도록 한다. 즉, 로그인을 한다.
  - 이름을 변경해서 사용하는 이유는 view 함수인 login 과의 혼동을 방지하기 위해 변경한다.

```python
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
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
{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}

<h1>로그인</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ form|crispy }}
    <input type="submit" value="Submit"/>
</form>
{% endblock %}
```

- 로그인 되었는지 확일할 방법이 없으니 다음과 같이 설정해본다.

  ```django
  <!-- base.html -->
  <body>
      <div class="container">
      <h1>현재 유저는 {{ user.username }} !</h1>
      <hr>
          {% block body %}
          {% endblock %}
      </div>
  ```

---

### 3. Logout

> [django User model](https://docs.djangoproject.com/en/2.1/ref/contrib/auth/#user-model)

- 로그아웃은 CRUD 에서 Session 을 Delete 하는 로직이다.

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('boards:index')
```

```python
# accounts/urls.py
path('logout/', views.logout, name='logout'),
```

---

### 4. 매끄럽게

#### 4.1 링크 분기

- `user.is_authenticated` 를 통해 로그인 되었는지를 판단할 수 있다.
- 이를 통해 템플릿을 매끄럽게 작업해보자.
  - 로그인과 비로그인 상태에서 보이는 링크를 다르게 변경.

```django
<!-- base.html -->
<body>
    <div class="container">
    {% if user.is_authenticated %}
        <h1>
            안녕, {{ user.username }}
            <a href="{% url 'accounts:logout' %}">로그아웃</a>
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

```django
<!-- boards/index.html -->
{% extends 'boards/base.html' %}
{% block body %}
<h1>게시글 목록</h1>
{% if user.is_authenticated %}
    <a href="{% url 'boards:create' %}">새 글 작성</a>
{% else %}
    <a href="{% url 'accounts:login' %}">새 글을 쓰려면 로그인 하세요.</a>
{% endif %}
```

#### 4.2 회원가입 후 바로 로그인 상태로 전환

- 현재 회원가입이 완료되면 로그인 되지 않은 상태로 index 페이지로 그냥 넘어간다.
- 그래서 회원가입과 동시에 로그인상태로 만들어 준다.

```python
# accounts/views.py
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()							# 1
            auth_login(request, user)				# 2
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
```

#### 4.3 로그인 되어 있으면 로그인/회원가입 페이지 못보게 설정

- 로그인 되어있는 상태라면 로그인과 회원가입 페이지에 접근 할 수 없도록 설정한다.

```python
# accounts/views.py
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
```

```python
# accounts/views.py
def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
```

---

### 5. 회원 탈퇴

- 로그인 상태에서만 회원 탈퇴 링크를 출력해서 회원정보를 삭제해보자.

  ```python
  # accounts/views.py
  def delete(request):
      user = request.user
      if request.method == 'POST':
          user.delete()
      return redirect('boards:index')
  ```

  ```python
  # accounts/urls.py
  path('delete/', views.delete, name='delete'),
  ```

  ```django
  <!-- boards/base.html -->
  <body>
      <div class="container">
      {% if user.is_authenticated %}
          <h1>
              안녕, {{ user.username }}
              <a href="{% url 'accounts:logout' %}">로그아웃</a>
              <form action="{% url 'accounts:delete' %}" method="post" style="display: inline;" onsubmit="return confirm('R U SURE?');">
                  {% csrf_token %}
                  <input type="submit" value="탈퇴">
              </form>
          </h1>
      {% else %}
  ```

---

### 6. 회원 수정

> [User model Fields](https://docs.djangoproject.com/ko/2.2/ref/contrib/auth/#user-model)
>
> [Custom UserChangeForm](<https://stackoverflow.com/questions/5521273/how-do-i-create-a-custom-userchangeform-that-does-not-allow-certain-fields-to-be>)
>
> [User 모델 참조하기 - User 모델을 직접 참조하지 말고 get_user_model() 을 사용해야 하는 이유](https://docs.djangoproject.com/ko/2.1/topics/auth/customizing/#referencing-the-user-model)

- 회원 정보를 수정하는 ModelForm 은 `UserChangeForm` 을 사용한다.

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import UserChangeForm
  
  def edit(request):
      if request.method == 'POST':
          form = UserChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('boards:index')
      else:
          form = UserChangeForm(instance=request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/edit.html', context)
  ```

  ```python
  # accounts/urls.py
  path('edit/', views.edit, name='edit'),
  ```

  ```django
  <!-- accounts/edit.html -->
  {% extends 'boards/base.html' %}
  {% block body %}
  {% load crispy_forms_tags %}
  
  <h1>회원 수정</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {{ form|crispy }}
      <input type="submit" value="Submit"/>
  </form>
  {% endblock %}
  ```

  ```django
  <!-- boards/base.html -->
  <body>
      <div class="container">
      {% if user.is_authenticated %}
          <h1>
              안녕, {{ user.username }}<br>
              <a href="{% url 'accounts:edit' %}">회원수정</a>
  ```

- 하지만, User 모델을 바탕으로 만들어진 UserChangeForm 을 그대로 가져다가 사용하면, 일반 사용자가 접근해서는 안될 필드까지 모두 수정이 가능해진다.

- 그래서 우리는 UserChangeForm 을 상속받아 새로운 `UserCustomChangeForm` 을 만들어 필요한 필드를 조정해야 한다.

  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserChangeForm 
  from django.contrib.auth import get_user_model
  
  class UserCustomChangeForm(UserChangeForm):
      class Meta:
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name',)
  ```

  ```python
  # accounts/views.py
  from .forms import UserCustomChangeForm
  
  def edit(request):
      if request.method == 'POST':
          form = UserCustomChangeForm(request.POST, instance=request.user)
          if form.is_valid():
              form.save()
              return redirect('boards:index')
      else:
          form = UserCustomChangeForm(instance=request.user)
      context = {
          'form': form,
      }
      return render(request, 'accounts/edit.html', context)
  ```

- 회원정보가 수정되었는지 admin 페이지에서 확인해보자.

---

### 7. 비밀번호 변경

> [PasswordChangeForm](https://docs.djangoproject.com/en/2.2/topics/auth/default/#django.contrib.auth.forms.PasswordChangeForm)
>
> [How to Create a Change Password View](https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html)

- 회원정보 수정을 위한 `UserChangeForm` 에도 password 필드가 있지만 막상 필드를 확인해보면 수정할 수 없다.

- 대신 form 가장 하단에 **다만 [이 양식](#)으로 비밀번호를 변경할 수 있습니다.** 라는 문구가 있는데 이 링크를 클릭하면 `accounts/password/` 라는 주소로 이동된다. django 가 기본적으로 설정하고 있는 링크이다. (우리가 app 이름을 accounts 로 했던 이유중 하나)

- 그래서 우리는 비밀번호 변경을 위해, django 가 기본적으로 제공하는 `PasswordChangeForm` 을 사용해서 위 링크와 연결해 구성하면 된다.

  - `PasswordChangeForm` 은 user objects 를 키워드 없이(instance) 없이 받는다. 비밀번호 변경은 반드시 user 가 있어야 하기 때문이다.

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
  
  def change_password(request):
      if request.method == 'POST':
          form = PasswordChangeForm(request.user, request.POST) # 인자 순서 유의
          if form.is_valid():
              user = form.save()
              return redirect('boards:index')
      else:
          form = PasswordChangeForm(request.user)	# PasswordChangeForm 는 instance 사용 안함
      context = {'form': form}
      return render(request, 'accounts/change_password.html', context)
  ```

  ```python
  # accounts/urls.py
  path('password/', views.change_password, name='change_password'),
  ```

  ```django
  <!-- accounts/change_password.html -->
  {% extends 'boards/base.html' %}
  {% block body %}
  {% load crispy_forms_tags %}
  
  <h1>비밀번호 변경</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {{ form|crispy }}
      <input type="submit" value="Submit"/>
  </form>
  {% endblock %}
  ```

- 비밀번호가 변경 된 것 같은데 무언가 이상하다. 로그인이 풀려버렸다.
- 비밀번호가 변경되면서 기존 세션에 있는 회원 인증 정보가 일치하지 않아졌기 때문이다.
- 따라서 `update_session_auth_hash` 라는 새로운 함수를 사용한다.

> `update_session_auth_hash`
>
> - 현재 사용자의 인증 세션이 무효화되는 것을 막고, 다시 로그인하지 않아도 될 수 있도록 세션을 유지한 상태로 업데이트 한다.

```python
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST) # 인자 순서 유의
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)	# PasswordChangeForm 는 instance 사용 안함
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)
```

---

### 8. Authorization(권한)

> [The `login_required` decorator](https://docs.djangoproject.com/ko/2.1/topics/auth/default/#the-login-required-decorator)

1. 로그인 상태에서만 글을 작성/수정
   - `@login_required` 는 해당 view 함수를 실행하려면 로그인이 필요하다는 설정이다.

```python
# boards/views.py
from django.contrib.auth.decorators import login_required

@login_required
def create(request):

@login_required 
def update(request, board_pk):
```

2. next
   - 비로그인 상태로 주소창에 직접 `/boards/new/` 를 입력해서 강제로 접속해보자. 위 설정 덕분에 새 글을 작성하는 페이지 대신 로그인 페이지가 출력된다.
   - 하지만 url 모습을 보면 `/accounts/login/?next=/boards/new/` 처럼 next 뒤쪽으로 주소가 추가적으로 생성되어있다.
   - 이것은 현재 페이지 작업 후에 **어디로 보낼 건지 미리 주소가 설정**되어 있는 것이다.
   - 우리가 주소창으로 접근하려고 했던 그 주소가 로그인이 되어있지 않으면 볼 수 없는 주소라서, django 가 로그인 페이지로 강제로 돌려보냈는데 우리가 로그인을 다시 정상적으로 하면 우리가 원래 요청했던 주소로 보내주기 위해 keep 해주는 것이다.
   - 따로 처리해주지 않으면 우리가 view 함수에 설정한 redirect 로 이동하게 되지만, next 에 저장된 주소를 작동시키기 위해 추가적인 작업을 해보자.
   - 다음 2 줄의 코드를 추가한다.
     - `request.POST.get('next')` / `'next': request.GET.get('next', '')`

```python
# accounts/views.py
def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.POST.get('next') or 'boards:index')  # 2
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
        'next': request.GET.get('next', '')															# 1
    }
    return render(request, 'accounts/login.html', context)
```

```django
<!-- accounts/login.html -->
{% extends 'boards/base.html' %}
{% block body %}
{% load crispy_forms_tags %}

<h1>로그인</h1>
<form action="" method="POST">
    {% csrf_token %}
    {{ form|crispy }}
    <input type="submit" value="Submit"/>
    <input type="hidden" name="next" value="{{ next }}">
</form>
{% endblock %}
```

> 로그인 안 한 상태에서 **1) 그냥 로그인할 때**와 **2) boards/new/ 주소로 강제로 들어갔을 때** form 의 imput hidden 값 비교(관리자 도구로 hidden 에 value 값 있고 없고 차이를 확인한다.)
>
> - `'next': request.GET.get('next', '')`
>
>   > [Python Standard Library - dict.get](<https://docs.python.org/ko/3.7/library/stdtypes.html#dict.get>)
>   >
>   > [Not using `get()` to return a default value from a dict](<https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html>)
>
>   - `dict.get()`
>
>     ```python
>     >>> dictionary = {"key": "hello"}
>     
>     # 1
>     >>> data = dictionary.get("test", "")
>     >>> data
>     >>> ''
>     
>     # 2
>     >>> data = dictionary.get("test")
>     >>> data
>     >>> type(data)
>     >>> NoneType
>     
>     # 3
>     >>> data = dictionary.get('key')
>     >>> data
>     >>> 'hello'
>     ```
>
>   - Bad
>
>     ```python
>     dictionary = {"message": "Hello, World!"}
>     
>     data = ""
>     
>     if "message" in dictionary:
>         data = dictionary["message"]
>     
>     print(data)  # Hello, World!
>     ```
>
>   - Good
>
>     ```python
>     dictionary = {"message": "Hello, World!"}
>     
>     data = dictionary.get("message", "")
>     
>     print(data)  # Hello, World!
>     ```

---

### 9. auth_form 합치기

- 현재 `change_password.html`, `edit.html`, `signup.html` 의  form 코드들이 모두 동일하다.

- `auth_form.html` 이란 이름으로 코드의 재사용성을 높여보자.

  ```django
  <!-- accounts/auth_form.html -->
  {% extends 'boards/base.html' %}
  {% block body %}
  {% load crispy_forms_tags %}
  
  {% if request.resolver_match.url_name == 'signup' %}
      <h1>회원가입</h1>
  {% elif request.resolver_match.url_name == 'edit' %}
      <h1>회원 수정</h1>
  {% else %}
      <h1>비밀번호 수정</h1>
  {% endif %}
  
  <form action="" method="POST">
      {% csrf_token %}
      {{ form|crispy }}
      <input type="submit" value="Submit"/>
  </form>
  {% endblock %}
  ```

- views.py 에 `signup, edit, change_password` 함수의 render template 링크를 모두 수정해준다.

---

### 10. User - Board

> [`Settings` REF](https://docs.djangoproject.com/en/2.1/ref/settings/#settings)
>
> [Settings - AUTH_USER_MODEL](https://docs.djangoproject.com/en/2.1/ref/settings/#auth-user-model)

- user 와 board 의 관계를 1:N 으로 만들어서 게시글을 작성할 때, 로그인 된 사람의 정보를 넣어 누가 작성했는지 함께 저장한다.
- 작성한 게시물(Board)에 user 정보를 추가한다. (`user : board = 1 : N`)
- django 에서 이미 만들어 놓은 user 모델을 가져오기위해 `settings` 를 활용한다.

```python
# boards/models.py
from django.conf import settings

class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

```BASH
$ python manage.py makemigrations

You are trying to add a non-nullable field 'user' to board without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1
Migrations for 'boards':
  boards/migrations/0002_board_user.py
    - Add field user to board
    
$ python manage.py migrate 
```

> 기존에 유저 없이 작성된 게시글에 user_id 컬럼에 default 값을 어떻게 할지 물어보는 문구가 나온다.
>
> 1을 입력하고 enter / 1(현재 admin user 번호) 을 다시 입력 후 enter

- 이 상태로 새 글을 작성하는 페이지를 보면 User 를 선택하는 input 도 함께 출력되기 때문에 아래와 같이 수정해야 한다.

  ```python
  # boards/forms.py
  class BoardForm(forms.ModelForm):
      class Meta:
          model = Board
          fields = ['title', 'content',]
  ```

#### 10.1 Create 로직 수정

- `commit=False` 는 **실제 db 에 반영 전까지의 단계**를 진행하고, 그 중간에 user 정보를 `request.user` 에서 가져와 저장한다.

  ```python
  # boards/views.py
  @login_required
  def create(request):
    	# print(request.user)		# user 정보 확인해보기
      if request.method == 'POST':
          form = BoardForm(request.POST)
          if form.is_valid():
              # board 를 바로 저장하지 않고 현재 user 정보를 넣고 저장
              board = form.save(commit=False)
              board.user = request.user
              board.save()
  ```

- 게시글을 작성한 user 가 누구인지 보기위해 `index.html` 수정

  ```django
  <!-- boards/index.html -->
  {% for board in boards %}
      <p><b>작성자 : {{ board.user }}</b></p>
      <p>{{ board.pk }}</p>
      <p>{{ board.title }}</p>
      <a href="{% url 'boards:detail' board.pk %}">글 보러가기</a>
      <hr>
  {% endfor %}
  ```

#### 10.2 UPDATE, DELETE 로직 수정

- 해당글의 게시자가 아니라면 삭제, 수정 버튼 가리기

  - user 에는 현재 사용자가 저장 되어있고, 해당 게시글의 작성자(board.user) 와 비교 후 버튼 출력/미출력

  ```django
  <!-- boards/detail.html -->
  {% if user == board.user %}
      <form action="{% url 'boards:delete' board.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="삭제">
      </form>
      <a href="{% url 'boards:update' board.pk %}">[수정]</a>
  {% endif %}
  ```

- 사용자가 자신의 글만 삭제/수정할 수 있도록 내부 로직 수정 (다른 유저의 게시글 수정/삭제 불가)

  ```python
  # boards/views.py
  @login_required 
  def update(request, board_pk):
      board = get_object_or_404(Board, pk=board_pk)
      if board.user == request.user:													# 1
          if request.method == 'POST':
              form = BoardForm(request.POST, instance=board)
              if form.is_valid():
                  board = form.save()
                  return redirect('boards:detail', board.pk)
          else:
              form = BoardForm(instance=board)
      else:
          return redirect('boards:index')											# 2
      context = {
          'form': form,
          'board': board,
      }
      return render(request, 'boards/form.html', context)
  ```

  ```python
  # boards/views.py
  def delete(request, board_pk):
      board = get_object_or_404(Board, pk=board_pk)
      if board.user == request.user:											# 1
          if request.method == 'POST':
              board.delete()
              return redirect('boards:index')
          else:
              return redirect('boards:detail', board.pk)
      else:
          return redirect('boards:index')									# 2
  ```
  