[TOC]

## fake_insta_04

**Content**

0. Hashtag
1. Social Login (with Kakao)

> 190422 Mon

---

### 0. Hashtag

#### 0.1 Create

- Hashtag 모델 생성
- *[주의]* Post 모델보다 상위에 있어야 Post 에서 참조가 가능하다.

```python
# posts/models.py
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
    
class Post(models.Model):
		...
    hashtags = models.ManyToManyField(Hashtag, blank=True)
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

```python
# posts/admin.py
from .models import Post, Hashtag

class HashtagAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Hashtag, HashtagAdmin)
```

```python
# posts/views.py
@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            # hashtag
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag[0])
	...
```

- 추가하는 코드는 `post.save()` 보다 하단에 와야한다.
- `get_or_create`의 return object 는 `(Hashtag instance, boolean)` 형태의 튜플이며, boolean에는 새로 만들어진 instance일 경우 `True`, 기존에 존재하던 instance일 경우 `False` 값이 온다.
- 게시글을 작성해보고 admin 페이지에서 Hashtag 가 잘 만들어졌는지 확인해보자.

#### 0.2 Update

- 수정 될 때는 기존의 hashtag 전체를 삭제한 후 다시 등록하는 과정이다.

```python
# posts/views.py
@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save()
            # hashtag
            post.hashtags.clear()
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag[0])
            return redirect('posts:list')
          ...
```

- 글을 수정 후 잘 동작했는지 admin 페이지에서  확인해보자.

#### 0.3 Hashtag 모아보기

- 해시태그를 클릭하면 해당 태그를 가진 게시물들을 모아서 보여줘야 한다.
- 아직 해시태그에 링크를 만들지 않아서 `posts/hashtag/1/` 이란 방식으로 확인해보자.
- 템플릿은 `people.html` 을 바탕으로 `hashtag.html` 을 만들고, 필요없는 부분을 삭제하고 알맞게 수정해보자.

```python
# posts/views.py
@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    posts = hashtag.post_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'posts': posts,
    }
    return render(request, "posts/hashtag.html", context)
```

```python
# posts/urls.py
path('hashtag/<int:hash_pk>/', views.hashtag, name='hashtag'),
```

```django
<!-- posts/hashtag.html -->
{% extends 'base.html' %}
{% block content %}
<h1 class="text-center">{{ hashtag.content }}</h1>
<div class="jumbotron jumbotron-fluid text-center mb-2 text-white bg-dark">
  <div class="container">
    <h1 class="display-4">{{ posts.count }} 개의 태그</h1>
    </div>
</div>
<hr>
<h3 class="text-center">{{ hashtag.content }} 를 태그한 글</h3>
<div class="row">
    {% for post in posts %}
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
{% endblock %}
```

#### 0.4 Hashtag 링크 연결

> [사용자 정의 템플릿 태그와 필터](https://docs.djangoproject.com/ko/2.1/howto/custom-template-tags/#custom-template-tags-and-filters)
>
> [Django 사용자 정의 필터 (Custom Template Filter)를 활용하여 인스타그램 해시태그 링크 구현하기]([https://wayhome25.github.io/django/2017/06/22/custom-template-filter/#2-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%A0%95%EC%9D%98-%ED%85%9C%ED%94%8C%EB%A6%BF-%ED%95%84%ED%84%B0-%EB%AA%A8%EB%93%88-%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B0](https://wayhome25.github.io/django/2017/06/22/custom-template-filter/#2-사용자-정의-템플릿-필터-모듈-작성하기))

- 현재 post 의 content 는 전체 내용이 출력된다.
- 이중에서 해시태그에 해당되는 부분만 링크를 걸어주기위해 커스텀템플릿필터를 만들어서 사용해야 한다.

> **template filter**
>
> - html에서 우리는 파이썬 문법을 사용하는게 아니라 DTL을 사용하고 있다.
> - 따라서 django 의 함수를 그대로 사용할 수 없다.
> - `| (파이프)` 뒤에 나오는게 template filter 다.
> - 이걸 우리 입맛대로 새로 커스텀해서 사용할 수 있다.
>
> ```django
> <!-- example -->
> {{ value|date:"D d M Y" }}
> ```

1. posts 앱 안에 `templatetags` 폴더 생성 (**폴더명은 반드시 `templatetags` !**)

2. templatetags 폴더안에 `__init__.py` 파일 생성 (이 폴더를 **패키지 모듈**로서 사용할 수 있도록 해준다.)

3. templatetags 폴더안에 `posts_templatetag.py` 생성 (이 파일명은 아무이름이나 상관 없다.)

4. templatetags 폴더를 추가하고나서 반드시 **서버를 재시작** 해야 한다.

   > After adding the `templatetags` module, you will need to restart your server before you can use the tags or filters in templates.
   >
   > ```
   > posts/
   >     __init__.py
   >     models.py
   >     templatetags/
   >         __init__.py
   >         posts_templatetag.py
   >     views.py
   > ```

```python
# posts/templatetags/posts_templatetag.py
from django import template
import re

register = template.Library()

# 1
@register.filter
def hashtag_link(post):
    content = post.content
    hashtags = post.hashtags.all()

    for hashtag in hashtags:
        content = re.sub(fr'{hashtag.content}\b', f'<a href="/posts/hashtags/{hashtag.pk}/">{hashtag.content}</a> ', content) # 마지막 공백 주의

    return content


# 2 - @hyeri
@register.filter
def hashtag_link(post):
    content = post.content + ' '
    hashtags = post.hashtags.all()
    
    for hashtag in hashtags:
        content = content.replace(hashtag.content+' ', f'<a href="/posts/hashtag/{hashtag.pk}/">{hashtag.content}</a> ')	# 마지막 공백 주의

    return content
```

> `\b` 단어 경계. 즉 단어 경계에서 딱 끝나는 단어를 파악한다.

- `hashtag_link` 라는 이름의 함수를 정의한다. (이건 템플릿에서 사용할 커스텀 필터의 이름이다.)
- 해당 post 가 가지고 있는 모든 hashtags 를 순회하며,
- content 내에서 해당 문자열(해시태그)을 링크를 포함한 문자열로 replace 한다.
  - `ex) #스타벅스 => <a href="/posts/hashtag/1/">#스타벅스</a>`
- 원하는 문자열로 replace 가 완료된 content 를 return 한다.

```django
<!-- posts/_post.html -->
{% load posts_templatetags %}

...

<!-- 기존 코드 -->
<p class="card-text">{{ post.content }}</p>
<!-- 변경 코드 -->
<p class="card-text">{{ post|hashtag_link|safe }}</p>
```

- 템플릿 최상단에 우리가 만든 커스텀 템플릿 파일명을 `load` 해준다.
- DTL 에서 filter 의 인자는 `| (파이프)` 앞에 변수가 인자로 들어간다.
  - 현재 우리 코드에서는 `hashtag_link(post)` 로 동작한다.
- `safe` 필터를 적용해야 실제 html 코드로 보여진다. (tag escape 방지)

---

### 1. Social Login

#### 1.1 사전작업

> [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
>
> - 위 공식 문서를 참고해서 진행한다.
>
> [wikidocs OAuth-allauth](https://wikidocs.net/9942#django-allauth)

```bash
$ pip install django-allauth
```

- settings.py

  ```python
  AUTHENTICATION_BACKENDS = (
      # Needed to login by username in Django admin, regardless of `allauth`
      'django.contrib.auth.backends.ModelBackend',
  )
  
  INSTALLED_APPS = [
    	...
      'django.contrib.sites',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.kakao',
    ...
  ]
  
  SITE_ID = 1
  ```
  
  > SITE_ID 값을 반드시 넣어야하는 이유.
  >
  > 이는 우리가 django.contrib.sites 앱을 설치하고 처음으로 레코드를 추가하면 PK가 1이기 때문입니다. 만약에 이 PK값을 변경하면 그에 맞춰서 수정해줘야 합니다.
  > 출처: <https://www.pincoin.co.kr/blog/www/32/django-disqus-설치-사용법/?page=1>
- insta/urls.py

  - **기존 accounts 주소보다 하단에 있도록 한다.**

  ```python
  # insta/urls.py
  urlpatterns = [
      path('accounts/', include('accounts.urls')),
      path('accounts/', include('allauth.urls')),		# 추가
      path('posts/', include('posts.urls')),
      path('admin/', admin.site.urls),
      path('<str:username>/', accounts_views.people, name='people'),
  ]
  ```

```bash
$ python manage.py migrate
```

- 새로운 경로들이 추가된 것을 확인 하기 위해 http://127.0.0.1:8000/accounts/ 로 이동해본다.
  - 1번부터 8번까지가 우리가 구현한 url 나머지는 `allauth.urls` 에서 만들어준 url 이다.
  - 모양이 이상한 이유는 장고 1.X 기준의 url 경로이기 때문이며, 정규표현식인데 몰라도 상관없다.
  - 우리가 구현한 `accounts/login`, `allauth.urls`에서 구현해준 `accounts/login` 중복이 되는데 위에서부터 처리되기 때문에 아래껀 신경 쓰지 않아도 된다. 

- 이제 admin 페이지에 들어가보면 `소셜 계정` 이라는 새로운 app이 생성되었다.

#### 1.2 KAKAO OAuth

> [https://developers.kakao.com](https://developers.kakao.com/)

1. 카카오 개발자 센터 로그인 후 앱 만들기 (아이콘은 없어도 무방)
2. 앱 생성 우측 `설정` ⇒ `일반` ⇒ `+플랫폼추가` 클릭
3. `웹` 선택  / 사이트도메인 `http://당신의주소.c9user.io/` 추가 (로컬이라면 `http://127.0.0.1:8000/` 를 입력한다. **c9은 반드시 8080 포트가 없어야한다.**)
4. Redirect Path 에 `/accounts/kakao/login/callback/` 추가
5. **Client ID** 는 `설정` ⇒ `일반` 에 REST API 키
6. **Secret Key** 는 `설정` ⇒ `고급` ⇒ `Client Secret`  코드생성 버튼 / 상태 ON
7. `설정` ⇒ `사용자 관리` 에서 프로필 정보 및 카카오 계정 on 으로 변경후, 수집목적은 아무거나 입력. 하나라도 빼먹으면 keyerror 오류 발생
8. django 서버에 id 와 key 를 등록하기 위해서 admin 페이지에서 `소셜 어플리케이션` 클릭
   1. 제공자 - Kakao
   2. name - 아무거나
   3. Client ID / Secret Key 입력
   4. 키 - 생략
   5. sites 에 현재 c9 서버 주소 입력 혹은 example.com 입력
   6. 저장

```django
<!-- accounts/login.html -->
{% extends 'base.html' %}
{% load bootstrap4 %}
{% load socialaccount %}

{% block content %}
<h1>로그인</h1>
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit="로그인" reset="Cancel" %}{% endbuttons %}
</form>
<!-- 카카오 로그인 추가 -->
<a href="{% provider_login_url 'kakao' method='oauth2' %}" class="btn btn-warning">카카오로그인</a>
{% endblock  %}
```

- 로그인 테스트를 해보면 자동으로 `accounts/profile/` 로 이동하게 된다.

- setting.py 에 로그인 후 어디로 갈지 설정하는 코드가 필요하다

  ```python
  LOGIN_REDIRECT_URL = 'posts:list'
  ```

- 여기까지 했을 때 문제가 있다. 카카오로 로그인한 유저의 마이페이지에서 `프로필 수정` 을 클릭하면, 해당 유저는 profile 이 없다고 한다. 

- 원래 정상적인 절차로 회원가입을 하면 user 가 생성되면서 빈 profile 을 가지고 생성되지만, 소셜 로그인으로 로그인된 경우 정상적인 회원가입 절차를 거치지 않고 가입되면서 자동 로그인 되기 때문이다. 

- 그리고 이렇게 생성된 user 는 db에  `accounts_user` 테이블과  `socialaccount_socialaccount` 에 저장된다.

- 그래서 profile 이 없는 경우 인스턴스를 생성하도록 처리해야한다.

  - `.get_or_create()` 사용

  ```python
  # accounts/views.py
  @login_required
  def profile_update(request):
      profile = Profile.objects.get_or_create(user=request.user) # 해당코드 추가
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

  - 다시 프로필 수정을 누르면 정상적으로 프로필을 수정할 수 있게 된다.


