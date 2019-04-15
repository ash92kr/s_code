## Django_03

**Content**

0. [crud start](#0-crud-start)
1. [Model](#1-model)
2. [DB API](#2-db-api)
3. [CREATE](#3-create)
4. [READ](#4-read)
5. [POST](#5-post)
6. [Django Admin](#6-django-admin)
7. [Django Extensions](#7-django-extensions)

> 190220 Wed

---

### 0. crud start

#### 0.1 `crud` project

- 프로젝트 시작

```bash
$ mkdir PROJECT02
$ cd PROJECT02
$ pyenv local django-venv 
$ django-admin startproject crud .
```

- settings.py 설정
  - ALLOWED_HOSTS / LANGUAGE_CODE / TIME_ZONE
- git / gitignore 설정
- 기본 설정 완료 후 로켓 페이지 확인하기

#### 0.2 `boards` App

- 어플리케이션 만들기

```bash
$ python manage.py startapp boards
```

- setting.py

```python
INSTALLED_APPS = [
    'boards.apps.BoardsConfig',	# or 'boards'
    ...,
]
```

---

### 1. Model

Django 는 기본적으로 SQLite 를 사용하도록 구성되어있다. (별도 설치 필요 X)

다른 데이터베이스를 사용하려면 [데이터베이스 연결](https://docs.djangoproject.com/ko/2.1/topics/install/#database-installation) 을 설치하고 그에 맞게끔 settings.py 를 다음과 같이 수정해야 한다.

- settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'django.db.backends.oracle',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

> 데이터베이스로 sqlite 를 사용하지 않는 경우 USER, HOST, PASSWORD 같은 추가 설정이 반드시 필요하다.
>
> [DATABASES](https://docs.djangoproject.com/ko/2.1/ref/settings/#std:setting-DATABASES)

- `INSTALLED_APPS`

  > 현재 장고 인스턴스에서 활성화된 모든 어플리케이션들의 이름

  - `django.contrib.admin` : 관리자용 사이트
  - `django.contrib.auth` : 인증 시스템
  - `django.contrib.contenttypes` : 컨텐츠 타입을 위한 프레임워크
  - `django.contrib.sessions` : 세션 프레임워크
  - `django.contrib.messages` : 메세징 프레임워크
  - `django.contrib.staticfiles` : 정적파일 관리 프레임워크

> 이 어플리케이션들은 기본으로 제공된다. 상황에 따라 미리 이 시점에서 데이터베이스 테이블을 만들 필요가 있다.

#### 1.1 Model 만들기

> **모델**이란 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)을 말한다.
>
> 사용자가 저장하는 데이터의 필수적인 필드들과 동작들을 포함하고 있다.

- models.py 

```python
class Board(models.Model):
    # id primary key 는 기본적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

> 1. `CharField(max_length=None, **options)`
>
> - **CharField 의`max_length` 는 필수 인자이다.**
>   - 필드의 최대 길이(문자 수)이며 데이터베이스 레벨과 Django 의 유효성 검사(값 검증)에서 사용된다.
> - 문자열 필드이며 작은사이즈부터 큰사이즈까지 사용된다. (많은 양의 텍스트에 경우는 TextField 를 사용)
>
> 2. `TextField(**options)`
>
> - A large size text field.
> - max_length 옵션을 주면 자동양식필드의 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않는다. (그럴 땐 CharField 를 사용한다.) 
>
> 3. `DateTimeField(auto_now=False, auto_now_add=False, **options)`
>
> - 생성일자 : `auto_now_add=True` 
>   - django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용
>
> - 수정일자 : `auto_now=True` 
>   - django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신
>
> https://docs.djangoproject.com/en/2.1/ref/models/fields/#datefield

- DB 컬럼과 어떤한 타입으로 정의할 것인지에 대에 `django.db.models` 를  활용해서 Board 클래스를 만든다.
- 각 모델은 `django.db.models.Model` 클래스의 서브클래스로 표현된다.
- 각각의 클래스 변수들은 **모델의 데이터베이스 필드**를 나타낸다.
- 기본 Not Null 조건이 붙는다.

> **USE_TZ**가 **True**일 때는 templates, forms 에서의 datetime 에만 사용자가 설정한 **TIME_ZONE**이 적용된다. 따라서 models 의 datetime 에는 이 부분이 적용되지 않았기 때문에 default 값인  'UTC'  로 계속 설정된다. models 에서도 사용자가 설정한 **TIME_ZONE** 값을 적용하고 싶다면 **False**로 바꿔야한다.

```python
# settings.py
USE_TZ = False
```

---

#### 1.2 Model 활성화

**1.2.1 makemigrations**

```bash
$ python manage.py makemigrations boards
# python manage.py makemigrations
```

> `makemigrations` 는 모델을 변경시킨 사실(혹은 새로운 모델을 만든 경우)과 이 변경사항을 migration 으로 저장시키고 싶다는 것을 장고에게 알린다. **(python 코드를 바탕으로 DB 설계도를 작성)**

> **TMI**
>
> **1. migration**
>
> - 장고가 모델의 변경사항을 저장하는 방법(실제 파일로 존재 ex. `boards/migrations/0001_initial.py`)
>
> **2. sqlmigrate**
>
> ```bash
> $ python manage.py sqlmigrate boards 0001
> ```
>
> ```sqlite
> BEGIN;
> --
> -- Create model Board
> --
> CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
> COMMIT;
> ```
>
> - app 이름과 migration 버전(0001, 0002, ..) 으로 명령어를 입력하면, **실제 데이터베이스에 적용되는 sql 쿼리문**을 확인 할 수 있다.
> - sqlmigrate 는 실제 데이터베이스를 migration 하지 않는다. (단순 결과 출력)
> - 테이블의 이름은 app 의 이름과 model 의 이름이 조합되어 자동으로 생성된다. (소문자)
> - PRIMARY KEY 는 자동으로 추가된다.
>
> **2. project 문제 검사**
>
> ```bash
> $ python manage.py check
> ```

- Board model 을 한번 더 수정하고 migration 을 진행해보자.

  ```python 
  class Board(models.Model):
  	...
      updated_at = models.DateTimeField(auto_now=True)
  ```

  ```bash
  $ python manage.py makemigrations boards
  ```

  ```bash
  $ python manage.py sqlmigrate boards 0002
  BEGIN;
  --
  -- Add field updated_at to board
  --
  ALTER TABLE "boards_board" RENAME TO "boards_board__old";
  CREATE TABLE "boards_board" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "updated_at" datetime NOT NULL, "title" varchar(10) NOT NULL, "content" text NOT NULL, "created_at" datetime NOT NULL);
  INSERT INTO "boards_board" ("id", "title", "content", "created_at", "updated_at") SELECT "id", "title", "content", "created_at", '2019-02-19 02:17:11.503225' FROM "boards_board__old";
  DROP TABLE "boards_board__old";
  COMMIT;
  ```

---

**1.2.2 migrate**

```bash
$ python manage.py migrate
# python manage.py migrate boards
```

- `migrate` 는 makemigrations 로 만든 설계도(migration)를 실제 DB 에 반영한다.
  이 과정으로 모델에서의 변경 사항들과 DB 의 스키마의 동기화가 이루어진다.

> Model 변경 순서
>
> 1. models.py 작성 및 변경
> 2. makemigrations : migration 만들기
> 3. migrate : DB 적용(테이블 생성)

**1.2.3 실제 db table 확인하기**

```bash
$ sqlite3 db.sqlite3
sqlite> .tables
auth_group                  boards_board              
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session            
auth_user_user_permissions           
```

- INSTALLED_APPS 중 몇몇은 최소 하나 이상의 DB 테이블을 사용하기 때문에 migrate 와 함께 테이블이 만들어진다.

---

### 2. DB API

- django shell

```bash
$ python manage.py shell
```

> 일반적인 python 인터프리터와 다르게 Django 에서 동작하는 모든 명령을 그대로 테스트해 볼 수 있다.

#### 2.1 Create

```python
from boards.models import Board
Board.objects.all()
>>> <QuerySet []>
```

> **QuerySet**, 쿼리셋
>
> - 전달 받은 모델의 객체 목록
> - 데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬을 할 수 있다.

```python
# INSERT INTO boards_board (title, content) VALUES ('hello', 'django!);

# 첫번째 방식
board = Board()
board.title = 'first'
board.content = 'django!'
board.save()

# 두번째 방식
board = Board(title='second', content='django!!')
boards.save() 

# 세번째 방식
Board.objects.create(title='third', content='django!!!')

# save()
# save 전까지는 db 에 저장이 안된다. (save 전 id, created_at 차이 비교)
board = Board()
board.title = 'fourth'
board.content = 'django!!!!'
board.id #none
board.created_at #none
board.save()
board.id
board.created_at

# save 전에 full_clean() 메소드를 통해 현재 board 객체가 validation(검증)에 적합한지를 알아 볼 수 있다.
>>> board = Board()
>>> board.title = 'asdqweasdzxczxxc'   # 앞으로 save() 방식으로 쓰는 이유!
>>> board.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/junhokim/.pyenv/versions/venv-django/lib/python3.6/site-packages/django/db/models/base.py", line 1152, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 15 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
```

#### 2.2 Read

```python
Board.objects.all()
>>> <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>, <Board: Board object (4)>]>
```

- 객체 표현 변경

```python
class Board(models.Model):
	...
    
    def __str__(self):
        return f"{self.id}: {self.title}"
```

> 객체의 표현을 인터프리터에서 편하게 보려는 이유도 있지만, admin 사이트에서도 객체의 표현이 사용되기 때문이다.
>
> *더블언더스코어는 던더(dunder, double-under)* 라고도 한다.

```python
from boards.models import Board
Board.objects.all()
>>> <QuerySet [<Board: 1: first>, <Board: 2: second>, <Board: 3: third>, <Board: 4: fourth>]>
```

```python
# SELECT * FROM boards;
boards = Board.objects.all()

# SELECT * FROM boards WHERE title='hello';
boards = Board.objects.filter(title='hello').all()
# SELECT * FROM boards WHERE title='hello' LIMIT 1;
board = Board.objects.filter(title='hello').first()

missing = Board.objects.filter(title='missing').first() #=> None

# get()
# SELECT * FROM boards WHERE id=1 LIMIT 1;
# PK 만 get으로 가져올 수 있다. (get 은 값이 중복이거나 일치하는 값이 없으면 오류가 나기 때문)
# 즉, PK 에만 사용하자.
# 리턴값은 board 객체이다.
board = Board.objects.get(pk=1)

# filter()
# get 으로 pk 를 가져오는 것과 다르게 QuerySet(리스트형식) 으로 가져오기 때문에 board.id 등으로 접근 불가.
# filter 자체가 여러 값을 가져올 수 잇다는 생각이 있기 때문에 장고가 몇개인지 보장을 못해서 0개, 1개라도 쿼리셋을 리턴한다.
board = Board.objects.filter(id=1)


# 장고 ORM 은 이름(title)과 필터(contains)를 더블언더스코어로 구분합니다.
# LIKE
boards = Board.objects.filter(title__contains='he').all()

# startwith
boards = Board.objects.filter(title__startswith='he')

# endswith
boards = Board.objects.filter(content__endswith='!')
# Board.objects.filter(content__endswith='!')[0]
# Board.objects.filter(content__endswith='!')[1]

# 이 아래 세 친구는 다른 것들과 조합해서 주로 사용된다.
# order_by
boards = Board.objects.order_by('title').all() # 오름차순
board = Board.objects.order_by('-title').all() # 내림차순

# limit & offset
# [offset:limit]
boards = Board.objects.all()[1:5]
```

#### 2.3 Update

```python
board = Board.objects.get(pk=1)
board.title = 'byebye'
board.save()
```

#### 2.4 Delete

```python
board = Board.objects.get(pk=1)
board.delete()
#=> (1, {'board.Board': 1})
```

> save() 메소드는  board 객체에 id 가 없을 때는 값을 추가(create)하고 있으면 수정(update)한다.

---

### 3. CREATE

- index

```python
def index(request):
    return render(request, 'boards/index.html')
```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]   
```

```python
# crud/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
```

- base(+bootstrap)

```django
<!-- boards/base.html -->
<body>
    <div class="container">
        {% block body %}
        {% endblock  %}
    </div>
</body>
```

```django
<!-- boards/index.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="/boards/new">글 작성하기</a>
	<hr>
{% endblock %}
```

- new

```python
# views.py
def new(request):
	return render(request, 'boards/new.html')
```

```python
# boards/urls.py
from django.urls import path
from . import views

urlpatterns = [
 path('new/', views.new, name='new'),
]
```

```django
{% extends 'boards/base.html' %}
{% block body %}
    <h1>NEW</h1>
    <form action="/boards/create/">
        <label for="title">Title</label>
        <input type="text" name="title" id="title" /><br>
        <label for="content">Content</label>
        <textarea name="content" id="content"></textarea>
        <input type="submit" value="Submit"/>
    </form
    <a href="/boards/">BACK</a>
{% endblock %}
```

- create

> **모듈 import 순서**
>
> ```python
> # 1. 파이썬 표준 라이브러리 ex) os, random..
> 
> # 2. Core django : 장고 프레임워크에 있는 것
> from django.shortcuts import render
> 
> # 3. 3rd party library ex) django extension, pip install
> 
> # 4. 장고 프로젝트 app
> from .models import Board
> # 명시적 상대 import vs 암묵적 상대 import (from model import Board)
> ```

```python
# views.py
from .models import Board

def create(request):
 	title = request.GET.get('title')
	content = request.GET.get('content')
   
	board = Board(title=title, content=content)
    board.save()
    
    # Board.objects.create(title=title, content=content)
	return render(request, 'boards/create.html')
```

```python
# boards/urls.py

urlpatterns = [
     path('create/', views.create, name='create'),
     path('new/', views.new, name='new'),
]
```

```django
<!-- boards/create.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>글이 작성되었습니다 !</h1>
{% endblock %}
```

---

### 4. READ

```python
# boards/views.py
def index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards': boards})
```

```django
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="/boards/new">글 작성하기</a>
    <hr>
    {% for board in boards %}
        <p>{{ board.id }}</p>
        <p>{{ board.title }}</p>
        {{ board.created_at|timesince }} 전
        <hr>
    {% endfor %}
{% endblock %}
```

```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    board = Board(title=title, content=content)
    board.save()
    # Board.objects.create(title=title, content=content)
    
    return render(request, 'boards/index.html') 
```

> 게시글 정렬 바꾸기
>
> ```python
> def index(request):
>     # boards = Board.objects.all()[::-1]	# 원래 결과를 바꿔서 파이썬이 변경
>     boards = Board.objects.order_by('-id')  # db 가 처음부터 바꿔서 전달
>     return render(request, 'boards/index.html', {'boards': boards})
> ```

---

### 5. POST

INDEX 페이지로 넘어가지만 작성한 글 목록들이 보이지 않는다. url 을 살펴보면  `https://django-intro-wnsgh6315.c9users.io/create/?title=반갑습니다&content=안녕안녕` 로 되어 있다. index 로 직접 접속하면 글이 잘 작성된 것을 확인 할 수 있다. 그런데 살짝 어색하다.

처음에 글이 보이지 않았던 이유는 보여지는 페이지 자체는 index 이지만 `https://django-intro-wnsgh6315.c9users.io/index/` url 로 돌아가 못했기 때문이다. 즉, 단순히 html 문서만 보여준 것이다.

create 는 model 의 record 를 생성해! 라는 요청이기 때문에 페이지를 달라고 하는 get 보다 post 가 의미상 적절하다. (그리고 모델과 관련된 데이터이기 때문에 url 에 직접 보여지는 것은 좋지 않다.)

```django
<!-- boards/new.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>NEW</h1>
    <form action="/boards/create/" method="POST">
        {% csrf_token %}
        <label for="title">Title</label>
        <input type="text" name="title" id="title" /><br>
        <label for="content">Content</label>
        <textarea name="content" id="content"></textarea>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}
```

그리고 POST 는 단순히 HTML 문서를 달라는 것이 아닌 **어떠한 요청을 처리해달라**는 것이기 때문에 board 가 생성되었는지 확인 가능한 다른 페이지(ex. index, show...) 로 넘겨주는게 일반적이다.

그래서 render 보다는 `redirect` 를 사용하자.

```python
from django.shortcuts import render, redirect, reverse, resolve_url


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title, content=content)
    board.save()
    # Board.objects.create(title=title, content=content)
    
    return redirect('/boards/')
    # return redirect(index)
```

---

### 6. Django Admin

- 사이트 방문자를 위한 것이 아닌, 사이트 관리자를 위한 페이지.
- Board 테이블을 `admin.py` 에 등록하고, 생성된 record 들을 관리 할 수 있는 기능 제공한다.
- 개발 단계에서 record 가 잘 생성 되었는지 확인 할 때 유용하다.

#### 6.1 관리자 생성

```bash
$ python manage.py createsuperuser
```

```bash
# 원하는 대로 관리자 계정을 만든다.
Username: admin

Email address: admin@gmail.com

Password: (보안상 입력해도 아무것도 출력되지 않음)
Password (again): 

Superuser created successfully.
```

> 그런데 관리자 사이트에 board app 이 보이지 않는다. 관리자 사이트에 board app 이 있다고 알려줘야 한다.

#### 6.2 관리 사이트에 app 등록

```python
# boards/admin.py
from django.contrib import admin
from .models import Board # 명시적 상대경로 표현 / model 경로도 동작하지만 이렇게 불러오는게 관용적

# Register your models here.
admin.site.register(Board)
```

> 이제 Board 를 관리자 사이트에서 확인하고 수정할 수 있다.

#### 6.3 관리 사이트 추가 사항

- 더 편하게 보기 위해서 아래처럼 작성하면 실제 Column 명과 내용을 바로 볼 수 있다.
- `list_display` 는 약속된 변수명이다.

```python
from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at','updated_at',)

admin.site.register(Board, BoardAdmin)
```

---

### 7. Django extensions

[django-extensions](https://pypi.org/project/django-extensions/)

- Django Extensions is a collection of custom extensions for the Django Framework.
- 기본 기능보다 향상된 확장 기능들을 제공한다.

```bash
# install
$ pip install django-extensions
# $ pip install django_extensions
```

```python
# settings.py
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```

- **shell_plus**
  - 기본 django-shell 보다 보다 편리한 확장프로그램
  - shell 이 실행되면서 현재 프로젝트에서 사용하고 있는 모든 모듈을 자동으로 import 해준다.

```bash
$ python manage.py shell_plus
```

```bash
# 예시
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from boards.models import Board
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.6.7 (default, Dec  9 2018, 17:28:26) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

---

```bash
PROJECT02
├── boards
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_board_updated_at.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── templates
│   │   └── boards
│   │       ├── create.html
│   │       ├── index.html
│   │       └── new.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── crud
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```











