[TOC]

## fake_insta_03

**Content**

0. 회원 수정
1. 회원 탈퇴
2. 비밀번호 변경
3. Profile (1:1)
4. Follow

> 190417 Wed

---

### 0. 회원 수정

- 로그인을 해야 회원정보를 수정할 수 있으니, `@login_required` 데코레이터를 사용한다.

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth.decorators import login_required
  
  @login_required
  def update(request):
      if request.method == 'POST':
          pass
      else:
          user_change_form = UserChangeForm(instance=request.user)
      context = {'user_change_form': user_change_form,}
      return render(request, 'accounts/update.html', context)
  ```

  ```python
  # accounts/urls.py
  path('update/', views.update, name='update'),
  ```

  ```django
  <!-- accounts/update.html -->
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  
  {% block content %}
  <h1>회원 수정</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form user_change_form %}
      {% buttons submit="회원수정" reset="Cancel" %}{% endbuttons %}
  </form>
  {% endblock  %}
  ```

- 이 상태로 `/accounts/update/` 로 접속해보면 일반 사용자가 수정하면 안되는 것들까지 모두 수정하도록 출력된다.

- 그래서 우리는 별도로  `UserChangeForm` 을 Custom 해야 한다.

  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth import get_user_model
  
  class CustomUserChangeForm(UserChangeForm):
      class Meta:
          model = get_user_model()
          fields = ['email', 'first_name', 'last_name',]
  ```

- `CustomUserChangeForm` 으로 바꾸고 폼이 제대로 나오는지 확인해본다.

  ```python
  # accounts/views.py
  from .forms import CustomUserChangeForm
  
  @login_required
  def update(request):
      if request.method == 'POST':
          pass
      else:
          user_change_form = CustomUserChangeForm(instance=request.user)
      context = {'user_change_form': user_change_form,}
      return render(request, 'accounts/update.html', context)
  ```

- 이제 실제 회원 정보를 수정하는 로직을 완성해보자.

  ```python
  # accounts/views.py
  @login_required
  def update(request):
      if request.method == 'POST':
          user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
          if user_change_form.is_valid():
              user_change_form.save()
              return redirect('people', request.user.username)
      else:
          user_change_form = CustomUserChangeForm(instance=request.user)
      context = {'user_change_form': user_change_form,}
      return render(request, 'accounts/update.html', context)
  ```

- 회원수정 페이지로 가능 링크를 people 페이지에 작성해보자.

  - 현재 people 페이지의 user 가 본인이라면, '정보 수정' 링크가 뜨도록 하면 자연스럽다.

  ```django
  <!-- accounts/people.html -->
  <h1 class="text-center">{{ people.username }}'s Profile</h1>
  {% if user == people %}
  <div class="text-center">
      <a href="{% url 'accounts:update' %}" class="badge badge-info">정보 수정</a>
  </div>
  {% endif %}
  ```

---

### 1. 회원 탈퇴

- 마찬가지로 로그인한 유저만 삭제하도록 작성한다.

  ```python
  # accounts/views.py
  @login_required
  def delete(request):
      if request.method == 'POST':
          request.user.delete()
      return redirect('posts:list')
  ```

  ```python
  # accounts/urls.py
  path('delete/', views.delete, name='delete'),
  ```

- 회원 수정 페이지에 탈퇴 버튼을 작성한다.

  ```django
  <!-- accounts/update.html -->
  ...
  <hr>
  <form action="{% url 'accounts:delete' %}" method="POST" onsubmit="return confirm('Are you sure ?')">
      {% csrf_token %}
      <a href="{% url 'people' user.username %}" class="btn btn-info">Back</a>
      <button type="submit" class="btn btn-danger">회원탈퇴</button>
  </form>
  {% endblock  %}
  ```

---

### 2. 비밀번호 변경

- `PasswordChangeForm(request.user)` 처럼 어떤 User 의 비밀번호를 변경하는지에 대한 정보도 같이 넘겨주어야 한다.

  ```python
  # accounts/views.py
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
  from django.contrib.auth import get_user_model, update_session_auth_hash
  
  @login_required
  def password(request):
      if request.method == 'POST':
          password_change_form = PasswordChangeForm(request.user, request.POST)
          # PasswordChangeForm(user=request.user, data=request.POST)
          if password_change_form.is_valid():
              user = password_change_form.save()
              update_session_auth_hash(request, user)
              return redirect('people', request.user.username)
      else:
          password_change_form = PasswordChangeForm(request.user)
      context = {'password_change_form': password_change_form,}
      return render(request, 'accounts/password.html', context)
  ```

  ```python
  # accounts/urls.py
  path('password/', views.password, name='password'),
  ```

  ```django
  <!-- accounts/password.html -->
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  
  {% block content %}
  <h1>비밀번호 변경</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form password_change_form %}
      {% buttons submit="변경" reset="Cancel" %}{% endbuttons %}
      <a href="{% url 'people' user.username %}" class="btn btn-info">Back</a>
  </form>
  {% endblock  %}
  ```

  ```django
  <!-- accounts/people.html -->
  <div class="text-center">
      <a href="{% url 'accounts:update' %}" class="badge badge-info">정보 수정</a>
      <a href="{% url 'accounts:password' %}" class="badge badge-warning">비밀번호 변경</a>
  </div>
  ```

- `update_session_auth_hash(request, user)` 

  > [Session invalidation on password change](https://docs.djangoproject.com/ko/2.1/topics/auth/default/#session-invalidation-on-password-change)

  - 현재 사용자의 인증 세션이 무효화되는 것을 막고, 다시 로그인하지 않아도 될 수 있도록 세션을 유지한 상태로 업데이트 한다.
  - 이 코드가 없다면, 비밀번호를 변경해보면 로그인이 풀린다. 비밀번호가 바뀌면서 기존의 세션에 있는 회원 인증 정보가 일치하지 않기 때문이다.

---

### 3. Profile (1:1)

#### 3.1 Create Profile Model

- User 모델은 계정과 관련된 핵심적인 정보들만 담겨있다.

- 상대적으로 가벼운 정보(닉네임, 자기소개 등)도 사용자로부터 받아 저장하고 싶을 때는 User 에 저장하는 것보다 Profile 이라는 모델을 따로 만들어 저장하는 것이 권장된다.

- 일반적으로 한명의 User 는 하나의 Profile 을 가지고 있기 때문에, `User : Profile = 1 : 1` 관계가 성립된다.

- Profile 모델의 모든 필드에 `blank=True` 옵션을 설정한다.

  - User 가 생성되면서 Profile 도 생성되는데, 그 시점에서는 닉네임과 자기소개를 입력하지 않았기 때문에 빈 값으로도 생성 될 수 있도록 하는 것이다.

  ```python
  # accounts/models.py
  from django.db import models
  from django.conf import settings
  
  # Create your models here.
  class Profile(models.Model):
      user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      nickname = models.CharField(max_length=40, blank=True)
      introduction = models.TextField(blank=True)
  ```

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

- 회원 가입, 즉 User가 생성됨과 동시에 Profile이 생성되어야 함으로 user의 create가 되는 view로 가서, profile을 생성하는 코드를 추가하자.

  ```python
  # accounts/views.py
  from .models import Profile
  
  def signup(request):
      if request.user.is_authenticated:
          return redirect('posts:list')
        
      if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              Profile.objects.create(user=user)		# 해당 코드 추가
              auth_login(request, user)
              return redirect('posts:list')
  	...
  ```

- admin 페이지에서 확인 할 수 있도록 추가해보자.

  ```python
  # accounts/admin.py
  from django.contrib import admin
  from .models import Profile
  
  class ProfileAdmin(admin.ModelAdmin):
      list_display = ['nickname', 'introduction', 'user_id',]
  admin.site.register(Profile, ProfileAdmin)
  ```

- 새롭게 회원가입을 해보고 user와 profile 모두 잘 생성 되었는지 확인해보자.

- 정상적으로 레코드가 생겼다면, 이 Profile 을 활용해서 User 의 프로필을 구성해 볼 것이다.

#### 3.2 Profile edit (Update)

- User 를 생성했기 때문에 create 는 필요없으며 update 만 필요하다.

- User 가 존재하는 이상 Profile 이 없을 일도 없으니 delete 도 필요하지 않다.

  ```python
  # accounts/forms.py
  from django import forms
  from .models import Profile
  
  class ProfileForm(forms.ModelForm):
      class Meta:
          model = Profile
          fields = ['nickname', 'introduction',]
  ```

  ```python
  # accounts/views.py
  from .forms import CustomUserChangeForm, ProfileForm
  
  @login_required
  def profile_update(request):
      if request.method == 'POST':
          profile_form = ProfileForm(request.POST, instance=request.user.profile)
          if profile_form.is_valid():
              profile_form.save()
              return redirect('people', request.user.username)
      else:
          profile_form = ProfileForm(instance=request.user.profile)
      context = {'profile_form': profile_form,}
      return render(request, 'accounts/profile_update.html', context)
  ```

  ```python
  # accounts/urls.py
  path('profile/update/', views.profile_update, name='profile_update'),
  ```

  ```django
  <!-- accounts/profile_update.html -->
  {% extends 'base.html' %}
  {% load bootstrap4 %}
  
  {% block content %}
  <h1>프로필 수정</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form profile_form %}
      {% buttons submit="수정" reset="Cancel" %}{% endbuttons %}
    <a href="{% url 'people' user.username %}" class="btn btn-info">Back</a>
  </form>
  {% endblock  %}
  ```

- 프로필을 수정하는 것이기 때문에 admin 페이지에서 각각 모든 user 에 프로필을 만들어 주지 않으면 **페이지에 접속 할 수 없다.** DB 를 초기화하거나 기존 user 모두에게 profile 을 만들어 주어야한다.

- 단, profile 모델 설정 이후로 회원가입하는 유저는 가입하면서 빈 profile 이 생성되기 때문에 정상적으로 페이지에 접속 할 수 있다.

- `프로필 수정` 링크를 people 페이지에 만들어보자.

  ```django
  <!-- accounts/people.html -->
  ...
  {% if user == people %}
  <div class="text-center">
      <a href="{% url 'accounts:update' %}" class="badge badge-info">정보 수정</a>
      <a href="{% url 'accounts:profile_update' %}" class="badge badge-success">프로필 수정</a>
      <a href="{% url 'accounts:password' %}" class="badge badge-warning">비밀번호 변경</a>
  </div>
  {% endif %}
  ...
  ```

- people 페이지에 프로필 정보가 출력되도록 하자. ([jumbotron](https://getbootstrap.com/docs/4.3/components/jumbotron/))

  ```django
  <!-- accounts/people.html -->
  ...
  <h1 class="text-center">{{ people.username }}'s Profile</h1>
  <div class="jumbotron jumbotron-fluid text-center mb-2">
    <div class="container">
      <h1 class="display-4">{{ people.profile.nickname }}</h1>
      <p class="lead">{{ people.profile.introduction }}</p>
    </div>
  </div>
  ...
  ```

---

### 4. Follow

> [맞춤 `User` 모델 대체하기](https://docs.djangoproject.com/ko/2.1/topics/auth/customizing/#substituting-a-custom-user-model)
>
> [Extending Django's default `User`](https://docs.djangoproject.com/ko/2.1/topics/auth/customizing/#extending-django-s-default-user)

- Follow는 User와 User의 M:N 관계이다. 그래서 이 관계를 정의하기 위해서는 User 모델을 수정해야하는데, 우리는 이때까지 django 에서 기본으로 제공하는 User 모델을 사용해왔고 그렇기에 직접 수정할 수는 없다.

- 그래서 새로운 User 모델을 만들어 쓸건데, 처음부터 만드는게 아니라 Django가 자신만의 User 모델을 만들 개발자들을 위해서 틀을 제공해준다! → `AbstractUser`

  > [AbstractUser vs AbstractBaseUser](https://whatisthenext.tistory.com/128)
  >
  > models.Model > AbstractBaseUser > AbstractUser > User
  >
  > AbstractBaseUser 를 상속받으면 password 와 last_login 만 기본적으로 제공한다. 그렇다면 custom 할 자유도는 높은거지만 그만큼 손 봐야할 것들이 너무 많다는 소리가 된다.

#### 4.1 User (`AbstractUser`)

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    # followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)
```

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'	# 기본 사용자 모델을 오버라이드
```

```python
# accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User

admin.site.register(User, UserAdmin)
```

- migrate 

  - 새로운 User 모델로 교체하기 위해서는 **Database를 완전 초기화** 해야한다. 아래 2가지를 반드시 수행하고 makemigrations, migrate 명령어를 입력하자.

    - accounts/migrations 폴더 안에, `__init__.py` 를 제외하고 모두 삭제한다.
    - `db.sqlite3` 파일을 삭제한다.

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

  - `accounts_user_followers` 라는 테이블이 생성된다.

    |  id  | from_user_id | to_user_id |
    | :--: | :----------: | :--------: |
    |  .   |      .       |     .      |

  - 그리고 database가 완전 초기화 되었으니 superuser도 새롭게 만들어 준다.

    ```bash
    $ python manage.py createsuperuser
    ```

- 서버를 켜서 회원가입을 하려고 하면 다음과 같은 에러가 발생한다.

  ```
  AttributeError at /accounts/signup/
  Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
  ```

- 이는 `UserCreateForm`에 설정된 모델이 django 기본 내장 User 모델로 되어있어서 발생하는 에러이다. (AuthenticationForm 과 같은 친구들은 알아서 get_user_model() 로 찾지만 `UserCreationForm` 과 `UserChangeForm` 은 기본 내장 User 모델로 설정되어 있어서 별도로 재작성하거나 확장해야 한다.)

  > [Custom users and the built-in auth forms](https://docs.djangoproject.com/ko/2.1/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms)

- 그래서 UserCreationForm을 재정의 해주어야 한다. (**forms 확장**)

  ```python
  # accounts/forms.py
  from django.contrib.auth.forms import UserChangeForm, UserCreationForm
  
  class CustomUserCreationForm(UserCreationForm):
      class Meta(UserCreationForm.Meta): # Meta class 도 상속 가능하다.
          model = get_user_model()
          fields = UserCreationForm.Meta.fields
  ```

- 회원가입(signup) view 함수를 수정해준다.

  ```python
  # accounts/views.py
  from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
  
  def signup(request):
      if request.user.is_authenticated:
          return redirect('posts:list')
        
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)		# 수정 1
          if form.is_valid():
              user = form.save()
              Profile.objects.create(user=user)
              auth_login(request, user)
              return redirect('posts:list')
      else:
          form = CustomUserCreationForm()		# 수정 2
      context = {'form': form}
      return render(request, 'accounts/signup.html', context)
  ```

- 이제 User 모델 교체가 완료되었고, User 와 User 의 M:N 관계도 정의되었다.

#### 4.2 Make Follow

```python
# accounts/views.py
@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)
```

```python
# accounts/urls.py
path('<int:user_pk>/follow/', views.follow, name='follow'),
```

```django
<!-- accounts/people.html -->
...
    <p class="lead">{{ people.profile.introduction }}</p>
    {% if user != people %}
        {% if user in people.followers.all %}
        <a href="{% url 'accounts:follow' people.pk %}" class="btn btn-outline-primary">Unfollow</a>
        {% else %}
        <a href="{% url 'accounts:follow' people.pk %}" class="btn btn-primary">Follow</a>
        {% endif %}
    {% endif %}
  </div>
</div>
```

> 자기 자신은 follow 하면 안된다. `user != people`

- profile 부분을 조금 더 정리해보자.

  - 해당 프로필 유저의 팔로워/팔로잉 수 출력
    - `팔로잉 : {{ people.followings.all.count }} / 팔로워 : {{ people.followers.all.count }}`
  - jumbotron 테마 변경
    - `text-white bg-dark`
  - `hr` 태그로 프로필 내용과 팔로우 부분 구분 짓기
    - `<hr class="my-4 border-white">`

  ```django
  <!-- accounts/people.html -->
  {% extends 'base.html' %}
  {% block content %}
  <h1 class="text-center">{{ people.username }}'s Profile</h1>
  <div class="jumbotron jumbotron-fluid text-center mb-2 text-white bg-dark">
    <div class="container">
      <h1 class="display-4">{{ people.profile.nickname }}</h1>
      <p class="lead">{{ people.profile.introduction }}</p>
      <hr class="my-4 border-white">
      <p class="lead">팔로잉 : {{ people.followings.all.count }} / 팔로워 : {{ people.followers.all.count }}</p>
      {% if user != people %}
          {% if user in people.followers.all %}
          <a href="{% url 'accounts:follow' people.pk %}" class="btn btn-outline-primary">Unfollow</a>
          {% else %}
          <a href="{% url 'accounts:follow' people.pk %}" class="btn btn-primary">Follow</a>
          {% endif %}
      {% endif %}
    </div>
  </div>
  ```

- 이제 list 페이지에서 **현재 로그인한 유저가 follow 한 사람들이 작성한 글만 출력**되도록 하자

  ```python
  # posts/views.pyㄴ
  @login_required
  def list(request):
      posts = Post.objects.filter(user__in=request.user.followings.all()).order_by('-pk')
      comment_form = CommentForm()
      context = {
          'posts': posts,
          'comment_form': comment_form,
          }
      return render(request, 'posts/list.html', context)
  ```

  > list 뷰함수에 `@login_required` 가 없다면 비로그인 상태에서 메인페이지를 볼 수 없다. 현재 로그인한 user 가 follow 하고 있는 사람들의 post 를 모두 가져오도록 했기 때문이다.
  >
  > **`Post.objects.filter(user__in=request.user.followings.all())`**
  >
  > - post 들을 가져올건데 user(현재 request.user 가 팔로잉하고 있는 user들)이 작성한 글들만 가져올거다.
  > - `.order_by('-pk')` : 최근에 작성된 글 순으로.
  > - [`QuerySet` API reference](https://docs.djangoproject.com/ko/2.1/ref/models/querysets/#queryset-api-reference)
  > - [Field lookups - `in`](https://docs.djangoproject.com/ko/2.1/ref/models/querysets/#in)
  > - [filter() vs filter().all()](https://stackoverflow.com/questions/22804252/django-orm-objects-filter-vs-objects-all-filter-which-one-is-preferre)

#### 4.3 Upgrade follow

**4.3.1 people 페이지 링크 연결**

- 다른 사람의 people 페이지로 가기가 쉽지 않다.

- 그래서 게시글 작성자를 클릭하면 해당 작성자의 people 페이지로 이동하도록 링크를 설정한다.

  ```django
  <!-- posts/_post.html -->
  <div class="col-10 my-3">
      <div class="card">
          <div class="card-header">
              <h5 class="card-text">
                  <a href="{% url 'people' post.user.username %}" class="card-link">{{ post.user }}</a>
              </h5>
            ...
  ```

**4.3.2 내 follow user 들의 글 + 내가 작성한 글**

- 현재 코드상태로는 내가 작성한 글이 나오지 않는다. 

- 내가 작성한 글도 follow 하고 있는 사람들의 글과 함께 볼 수 있도록 하자.

  ```python
  # posts/views.py
  from itertools import chain
  from django.db.models import Q
  
  @login_required
  def list(request):
      # 1. Q object 사용
      followings = request.user.followings.all()
      posts = Post.objects.filter(Q(user__in=followings) | Q(user=request.user.id)).order_by('-pk')
      
      # 2. Chain 사용
    	# 내가 follow 하고 있는 user의 리스트
      followings = request.user.followings.all()
      # followings 변수(쿼리셋)와 나(리스트 형식)를 묶음
      chain_followings = chain(followings, [request.user])
      # 이 사람들이 작성한 Post 들만 뽑아옴
      posts = Post.objects.filter(user__in=chain_followings).order_by('-pk')
      
      comment_form = CommentForm()
      context = {
          'posts': posts,
          'comment_form': comment_form,
          }
      return render(request, 'posts/list.html', context)
  ```

- 확인해보면 내가 follow 하고있는 유저들의 게시글과 내가 작성한 글이 모두 출력된다.

- `Q objects`

  > [Complex lookups with `Q` objects](https://docs.djangoproject.com/ko/2.1/topics/db/queries/#complex-lookups-with-q-objects)
  >
  > [쿼리 만들기](https://docs.djangoproject.com/ko/2.1/topics/db/queries/#making-queries)

- `itertools - chain()`

  > [itertools - doc](https://docs.python.org/ko/3.7/library/itertools.html#itertools.chain)
  >
  > [Django merging two QuerySet using itertools.](https://mushfiq.me/2013/08/04/django-merging-to-queryset-using-itertools/)
  >
  > [데이터 분석에 피가 되는 itertools 익히기](https://hamait.tistory.com/803)
  >
  > - 자신만의 반복자(iterator)를 만드는 모듈
  >
  > **`chain(*iterables)`**
  >
  > - iterable한 객체들을 인수로 받아 하나의 iterator로 반환한다.
  > - 리스트(list, tuple, itertables) 를 연결한다.
  > - 아래의 예시를 따라해보자.
  >
  > ```python
  > # shell_plus
  > from itertools import chain
  > 
  > >>> posts = Post.objects.all()
  > >>> posts
  > <QuerySet [<Post: asdasd>, <Post: asdasd>, <Post: qweqwe>, <Post: sadasd>]>
  > 
  > >>> images = Image.objects.all()
  > >>> images  
  > <QuerySet [<Image: Image object (1)>, <Image: Image object (2)>, <Image: Image object (3)>, <Image: Image object (4)>, <Image: Image object (5)>]>
  > 
  > ---
  > 
  > >>> all_chain = chain(posts, images)
  > >>> all_chain
  > <itertools.chain at 0x113478a58>
  > 
  > >>> type(all_chain)
  > itertools.chain
  > 
  > >>> list(all_chain)
  > [<Post: asdasd>,
  >  <Post: asdasd>,
  >  <Post: qweqwe>,
  >  <Post: sadasd>,
  >  <Image: Image object (1)>,
  >  <Image: Image object (2)>,
  >  <Image: Image object (3)>,
  >  <Image: Image object (4)>]
  > ```
  >
  > ```python
  > >>> chain('abc', 'def')
  > <itertools.chain at 0x113d62748>
  > 
  > >>> list(chain('abc', 'def'))
  > ['a', 'b', 'c', 'd', 'e', 'f']
  > ```
  >
  > ```python
  > >>> letters = ['a', 'b', 'c', 'd', 'e']
  > >>> numbers = [5, 4, 3, 2, 1]
  > 
  > >>> chain(letters, numbers)                                                                           
  > <itertools.chain at 0x113d86048>
  > 
  > >>> list(chain(letters, numbers))                                                                     
  > ['a', 'b', 'c', 'd', 'e', 5, 4, 3, 2, 1]
  > ```

**4.3.3 Explore page**

- 자연스럽지 못한 부분이 있다면, 내가 follow 하지 않은 사람들은 찾을 수도 없고 그들의 글도 볼 수 없다는 것이다.

- 그래서 **모든 게시글**이 출력되는 페이지를 만들어 보자.

  ```python
  # posts/views.py
  @login_required
  def explore(request):
      posts = Post.objects.order_by('-pk')
      comment_form = CommentForm()
      context = {
          'posts': posts,
          'comment_form': comment_form,
          }
      return render(request, 'posts/explore.html', context)
  ```

  ```python
  # posts/urls.py
  path('explore/', views.explore, name='explore'),
  ```

  ```django
  <!-- posts/explore.html -->
  {% extends 'base.html' %}
  {% block content %}
  <div class="d-flex flex-wrap justify-content-center">
      {% for post in posts %}
          {% include 'posts/_post.html' %}
      {% endfor %}
  </div>
  {% endblock  %}
  ```

  ```django
  <!-- posts/_nav.html -->
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark px-5 d-flex justify-content-between">
  	...
      {% if user.is_authenticated %}
  	...
          <div class="navbar-nav">
              <li class="nav-item">
                  <a href="{% url 'posts:explore' %}" class="nav-link">Explore</a>
              </li>
  	...
  ```

  > [번외] 만약 **내가 작성한 글을 제외한** 모든 게시글이 출력되는 페이지를 만든다면 아래와 같이 작성할 수 있다.
  >
  > ```python
  > posts = Post.objects.exclude(user=request.user).order_by('-pk')
  > ```
  >
  > **`exclude()`**
  >
  > [쿼리만들기 - Retrieving specific objects with filters](https://docs.djangoproject.com/ko/2.1/topics/db/queries/#retrieving-specific-objects-with-filters)
  >
  > - 특정 조건을 제외한 나머지 Record 들을 가져온다.