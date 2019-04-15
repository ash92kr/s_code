## Django_01

**Content**

[0. 준비 사항](#0-준비-사항)

[1. Django start](#1-django-start)

[2. MTV](#2-mtv)

[3. views-urls](#3-views-urls)

[4. Template](#4-template)

[5. Form](#5-form)

[6. Template Inheritance](#6-template-inheritance)

> 190213 Wed
>
> 👨‍💻 : 강의 commit 지점
>
> **Django: the Web framework for perfectionists with deadlines.**

---

### 0. 준비 사항

1.  pyenv / python / pyenv-virtualenv 설치 및 설정 [[참고]](https://zzu.li/djpy2_c9)

   - python 3.6.7
   - git
   - django 2.1.x

2. 가상환경 생성

   ```bash
   $ pyenv virtualenv 3.6.7 django-venv
   ```

3. 프로젝트 폴더 생성 및 이동

   ```bash
   $ mkdir PROJECT01
   $ cd PROJECT01
   ```

4. local 가상환경 활성화

   ```bash
   $ pyenv local django-venv
   (django-venv) $
   ```

5. django 설치

   ```bash
   $ pip install django
   ```

---

### 1. Django start

#### 1.1 django project

1. 프로젝트 생성

   > 가상 환경이 활성화 된 현재 폴더 안에 프로젝트를 생성. 명령어 마지막 `.` 주의.
   >
   > project 를 생성할 때, Python 이나 Django 에서 사용중인 이름은 피해야 한다.
   >
   > `-` 도 사용할 수 없다.
   >
   > (ex. django, test, class, django-test...)

   ```bash
   $ django-admin startproject django_intro .
   ```

2. 서버 실행

   ```bash
   $ python manage.py runserver $IP:$PORT
   # $ python manage.py runserver 0.0.0.0:8080
   ```

   > c9 에서는 Invalid HTTP_HOST header error 가 발생.
   >
   > - `settings.py` 에서 `ALLOWD_HOSTS` 와일드 카드 설정.
   >
   >   ```python
   >   ALLOWED_HOSTS = ['*'] 
   >   # 혹은
   >   ALLOWED_HOSTS = ['example-username.c9users.io'] 
   >   # https://, :8080 를 제외한 url
   >   ```
   >
   > - 다시 서버 실행 후 로켓 확인.

3. gitignore 설정

   ```bash
   $ touch .gitignore
   ```

   - https://www.gitignore.io/ 에서 django 를 선택해서 받은 코드를 `.gitingnore` 파일에 입력.

4. TIME_ZONE, LANGUAGE_CODE 설정

   - `settings.py`

     ```python
     LANGUAGE_CODE = 'ko-kr'
     TIME_ZONE = 'Asia/Seoul'
     ```

5. 서버 재실행 및 한글화 확인

> **상황에 따른 설정**
>
> 공식문서에 따르면, 단일 프로젝트에서는 `django-admin` 보다는 `manage.py`를 사용하는 것이 편할 것이라고 이야기한다. 기본적으로 후자는 프로젝트 경로를 시스템 path에 추가하며, settings.py 설정된 내용을 `DJANGO_SETTINGS_MODULE` 환경변수에 넣어서 활용한다. 
>
> 다만, 나중에 프로젝트 및 app 단위별로 setting이 나뉘게 된다면 이 경우에는 `django-admin` 명령어에 CLI 옵션 `--settings` 를 통해 지정하여 실행할 수 있는 장점이 있다.

👨‍💻 - "01_django setting and make app"

6. 프로젝트 구조

```
PROJECT01/
    manage.py
    django_intro/
        __init__.py
        settings.py
        urls.py
        wsgi.py
	db.sqlite3
```

- `PROJECT01/`: 디렉토리 바깥의 디렉토리는 단순히 프로젝트를 담는 공간. 이 이름은 Django 와 아무 상관이 없으니, 원하는 이름으로 변경이 가능.
- `manage.py`: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티. 
- `django_intro/`: 디렉토리 내부에는 project 를 위한 실제 Python 패키지들이 저장됨. 이 디렉토리 내의 이름을 이용하여, (`django_intro.urls` 와 같은 식으로) project 어디서나 Python 패키지들을 import 할 수 있다.
- `__init__.py`: Python 으로 하여금 이 디렉토리를 패키지 처럼 다루라고 알려주는 용도의 단순한 빈 파일.
- `settings.py`: 현재 Django project 의 모든 환경/구성을 저장. 
- `urls.py`: 현재 Django project 의 URL 선언을 저장. Django 로 작성된 사이트의 "목차". 사이트의 url 과 views 의 연결을 지정. 모든 url 매핑 코드가 포함될 수 있지만, 특정한 어플리케이션에 매핑의 일부를 할당해주는 것이 일반적.
- `wsgi.py`: 현재 project 를 서비스 하기 위한 WSGI 호환 웹 서버의 진입점.
  - `WSGI(Web server gateway interface)`: 파이썬 웹 프레임워크에서 사용하는 웹서버 규칙

#### 1.2 django application

> - 실제로 특정한 역할을 해주는 친구가 바로 application
> - 프로젝트는 이러한 어플리케이션의 집합이고, 실제 요청을 처리하고 페이지를 보여주고 하는 것들은 이 어플리케이션의 역할
> - 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있다.
>   - 어플리케이션은 하나의 역할 및 기능 단위로 쪼개는 것이 일반적이나 작은 규모의 서비스에서는 잘 나누지 않는다. 반드시 이렇게 나눠야 한다는 기준 또한 없다.
> - 각각의 어플리케이션은 MTV  패턴으로 구성되어 있다.

1. Application 만들기

   ```bash
   $ python manage.py startapp home
   ```

2. Application 구조

   ```
   home/
   	__init__.py
   	admin.py
   	apps.py
   	models.py
   	tests.py
   	views.py
   	migrations/
   		__init__.py
   ```

   - `admin.py` : 관리자용 페이지 커스터마이징 장소.
   - `apps.py` : 앱의 정보가 있는 곳. 우선 우리는 수정할 일이 없다.
   - `models.py` : 앱에서 사용하는 Model 를 정의하는 곳.
   - `tests.py` : 테스트 코드를 작성하는 곳.
   - `views.py` : view 들이 정의 되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현하는 곳.

3. Application 등록

   > - 방금 생성한 application 을 사용하려면 프로젝트에게 앱을 만들었다고 알려주어야 사용 가능하다.
   > - `home > apps.py > class HomeConfig()` 구조 이기 때문에 `home.apps.HomeConfig` 로 작성한다.

   - `settings.py`

     ```python
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'home.apps.HomeConfig',
     ]
     # 항상 `,`(쉼표) 를 작성해주고 마치는 습관을 가진다.
     # 혹은 그냥 'home' 이라고 작성할 수 있다. 다만, 후반부 자세한 설정에 한계가 있기 때문에 위처럼 작성한다.
     ```

---

### 2. MTV

- 장고를 제외하면 일반적으로 MVC 패턴으로 사용된다.
  - **M**odel : 어플리케이션의 핵심 로직의 동작을 수행한다. (Database)
  - **T**emplate(View) : 어떻게 데이터가 보여질지를 수행한다. (Interface)
  - **V**iew(Controller) : 어떤 데이터를 보여줄지를 구현한다. (Logic)

-  .py 3대장

  - `models.py` : 데이터베이스 관리
  - `views.py` : 페이지 관리 (페이지 하나 당, 하나의 함수)
  - `urls.py` : 주소(URL) 관리

  > flask 에서 app.py 한 곳에서 했던 걸, django 는 모두 나눠서 한다.

---

### 3. views-urls

> 우리는 앞으로 
>
> 1. views.py
> 2. urls.py
> 3. templates
>
> 순으로 코드를 작성할 것이다.

![img_01](images/img_01.png)

1. views 설정 (`home/views.py`)

   ```python
   from django.shortcuts import render, HttpResponse
   # 혹은 from django.http import HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpResponse('Welcome to Django !')
   ```

   > 여기서 우리가 접속해서 볼 페이지를 작성한다.

2. urls 설정 (`django_intro/urls.py`)

   ```python
   from django.contrib import admin
   from django.urls import path
   from home import views
   
   urlpatterns = [
       path('home/index/', views.index, name='index'),
       path('admin/', admin.site.urls),
   ]
   ```

   - 장고 서버로 요청(`request`)이 들어오면, 이 요청이 어디로 가야하는지 인식하고 관련된 함수(view)로 넘겨준다.

     ```python
     def index(request):
         # 실제로 어떤 값이 오는지 확인해보자.
         print(request) # <WSGIRequest: GET '/home/'>
         print(type(request)) # <class 'django.core.handlers.wsgi.WSGIRequest'>
         print(request.META)
     	return HttpResponse('Welcome to Django !')
     ```

   - 위에서부터 하나씩 검사하면서 찾기 때문에 순서가 중요하다. 아직은 이 순서 때문에 문제가 생기지 않지만 후에 복잡한 페이지가 만들면 이 순서가 중요해진다.

   - flask 에서 `app.route()`의 역할을 하나의 파일로 모아 놓은 것이다.

   > **path()** 함수 [[doc]](https://docs.djangoproject.com/ko/2.1/intro/tutorial01/#path-argument-route)
   >
   > - `path()`함수에는 2개의 필수 인수인 `route` 와 `view`, 2개의 선택 가능한 인수로 `kwargs` 와 `name` 까지 모두 4개의 인수가 전달된다. (`kwargs` 는 다루지 않는다.) 
   > - `path(route, view, name)`
   >
   > **HttpResponse**
   >
   > - HttpResponse(content='', content_type=None, status=200, reason=None, charset=None)
   > - Content 로 넘겨줄 수 있는 것은 iteraror 혹은 string 만 가능하다.
   >   - iterator 는 join 해서 string 으로 만들어서 넘겨주고, int 는 string 으로 형변환해서 넘겨준다.
   >
   > **나중에 url 을 나누게 된다면, 직접 app 에 urls.py 를 만들고 아래처럼 구조를 만든다.**
   >
   > ```python
   > # app url
   > from django.urls import path
   > from . import views
   > 
   > url patterns = [
   >  path('index/', views.index, name='index')
   > ]
   > ```
   >
   > ```python
   > # 프로젝트 url
   > from django.contrib import admin
   > from django.urls import include, path
   > 
   > urlpatterns = [
   >  path('home/', include('home.urls')),
   >  path('admin/', admin.site.urls),
   > ]
   > ```

3. 첫 메세지 출력 확인하기

   ```bash
   $ python manage.py runserver $IP:$PORT
   ```

👨‍💻 - "02_welcome django"

---

### 4. Template

> Django 에서 사용되는 Template 은 DTL(Django Template Language)이다.
>
> jinja2 와 문법이 유사하다.

#### 4.1 Template Variable

1. views 설정

   ```python
   import random 
   
   def dinner(request): 
       menus = ['pizza', 'bob', 'chicken', 'sushi']
   	pick = random.choice(menus)
       return render(request, 'dinner.html', {'menus': menus, 'pick': pick})
   ```

   > **render()**
   >
   > - `render(request, temaplate_name, context=None, content_type=None, status=None, using=None)`
   >   - 필수 인수 : request, template_name
   >   - 선택 인수 : context (**DTL 에서 사용될 변수를 딕셔너리**로 넘긴다.)

2. urls 설정

   ```python
   path('home/dinner/', views.dinner, name='dinner'),
   ```

3. template 설정

   ```django
   <h1> 오늘 저녁은 {{ pick }} !</h1>
   ```

   ```django
   	{% for menu in menus %}
           <p>{{ menu }}</p>
       {% endfor %}
       <hr>
       {% if pick == 'chicken' %}
           <p>푸라닭 !</p>
       {% else %}
           <p>{{ pick }}</p>
       {% endif %}
   ```

👨‍💻 - "03_template variable"

#### 4.2 Variable Routing

![img_02](images/img_02.png)

1. views 설정

   ```python
   def hello(request, name):
       return render(request, 'hello.html', {'name': name})
   ```

2. urls 설정

   ```python
   path('home/hello/<name>/', views.hello, name='hello'),
   ```

3. template 설정

   ```django
   <h1>{{ name }}, 안녕 ?!</h1>
   ```

**넘어 오는 숫자를 3제곱 리턴하는 실습**

```python
def cube(request, num):
    nums = num ** 3
    return render(request, 'home/cube.html', {'nums': nums, 'num': num})
```

```python
path('home/cube/<int:num>/', views.cube, name='cube'),
```

```django
<h1>{{ num }}의 세제곱은 {{ nums }}입니다. :)</h1>
```

👨‍💻 - "04_variable routing"

---

### 5. Form

#### 5.1 GET

1. ping

   1. views 설정

      ```python
      def ping(request):
          return render(request, 'ping.html')
      ```

   2. urls 설정

      ```python
      path('ping/', views.ping, name='ping'),
      ```

   3. templates 설정

      ```django
      <form action='/home/pong'>
          <input type="text" name="data"/>
          <input type="submit" value="Submit"/>
      </form>
      ```

2. pong

   1. views 설정

      ```python
      def pong(request):
          # print(request.GET) # <QueryDict: {'ping': ['AAA']}>
          data = request.GET.get('data')
          return render(request, 'pong.html', {'data': data})
      ```

   2. urls 설정

      ```python
      path('home/pong/', views.pong, name='pong'),
      ```

   3. template 설정

      ```django
      <h1>퐁~! {{ data }}</h1>
      ```

#### 5.2 POST

1. user_new

   1. views 설정

      ```python
      def user_new(request):
          return render(request, 'user_new.html')
      ```

   2. urls 설정

      ```python
      path('home/user_new/', views.user_new, name='new'),
      ```

   3. template 설정

      > - `{% csrf_token %}`
      > - post 는 url 끝에 슬래쉬(`/`) 필수

      ```django
      <form action='/home/user_create/' method='POST'> 
          {% csrf_token %}
          <input type="text" name="username"/>
          <input type="password" name="pwd"/>
          <input type="submit" value="Submit"/>
      </form>
      ```

2. user_create

   1. view 설정

      ```python
      def user_create(request):
          # print(request.POST)
          username = request.POST.get('username')
          pwd = request.POST.get('pwd')
          return render(request, 'user_create.html', {'username': username, 'pwd': pwd})
      ```

   2. urls 설정

      ```python
      path('home/user_create/', views.user_create, name='create'),
      ```

   3. templates 설정

      ```django
      <h1>username : {{ username }}</h1>
      <h2>password : {{ pwd }}</h2>
      ```

> **CSRF** 사이트 간 요청 위조(Cross-site Request Forgery) [doc](https://sj602.github.io/2018/07/14/what-is-CSRF/)
>
> > 2008 옥션 해킹(해커가 옥션 운영자에게 CSRF 코드가 포함된 이메일을 보내서 관리자 권한을 얻어냈다))
>
> - 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격방법을 의미한다.
> - 실제로 input type hidden 으로 특정한 hash 값이 담겨있는 것을 볼 수 있다.
> - `setting py` 에 middleware 설정에 보면 csrf 관련된 내용이 설정된 것을 볼 수 있다.
>
> **해당 csrf attack 보안과 관련된 설정은 `settings.py`에서 `MIDDLEWARE` 에 되어있다.**
>
> > Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.
>
> - 실제 토큰이 없을 때 오류가 raise 되는 시점을 보면 middleware 어쩌고저쩌고로 되어있다.
>
> ```python
> MIDDLEWARE = [
>  'django.middleware.security.SecurityMiddleware',
>  'django.contrib.sessions.middleware.SessionMiddleware',
>  'django.middleware.common.CommonMiddleware',
>  'django.middleware.csrf.CsrfViewMiddleware',
>  'django.contrib.auth.middleware.AuthenticationMiddleware',
>  'django.contrib.messages.middleware.MessageMiddleware',
>  'django.middleware.clickjacking.XFrameOptionsMiddleware',
> ]
> ```
>
> - 4번째 줄에 있는 csrf 를 주석처리하면 토큰이 없어도 되지만 그런 보안에 취약한 것은 하지말자.
>
> - Flask 보다 Django를 사용하는 이유도 기본적인 설정들을 통해 안정성 있고 편리한 개발을 할 수 있기 때문인 것. (플라스크가 Micro framework인 이유)
>
> - 실제로 [상단의 요청 과정 그림](#4.2 Variable Routing) 에서 `urls.py` 이전에 Middleware의 설정 사항들을 순차적으로 거친다. 응답은 아래에서 위로부터 미들웨어를 적용시킨다.
>
> > You can think of it like an **onion**: each middleware class is a "layer" that wraps the view, which is in the core of the onion. If the request passes through all the layers of the onion (each one calls `get_response` to pass the request in to the next layer), all the way to the view at the core, the response will then pass through every layer (in reverse order) on the way back out.

👨‍💻 - "05_form data GET POST"

---

### 6. Template Inheritance

- `home/templates/base.html` 만들기 (+bootstrap)

  > html 파일 모두 상속받게 수정하기

  ```django
  <!DOCTYPE html>
  <html lang="ko">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>{% block title %}{% endblock %}</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
  </head>
  <body>
      <h1>장고 연습</h1>
      <hr>
      <div class="container">
          {% block body %}
          {% endblock %}
      </div>
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

👨‍💻 - "06_template inheritance"