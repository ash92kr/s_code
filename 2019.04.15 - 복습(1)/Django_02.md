## Django_02

[TOC]

**Content**

0. [DTL](#0-dtl)
1. [static 파일 관리](#1-static-파일-관리)
2. [URL 설정 분리](#2-url-설정-분리)
3. [Template name spacing](#3-template-name-spacing)
4. [Template inheritance](#4-template-inheritance)
5. [디렉토리 구조](#5-디렉토리-구조)

> 190214 Thu
>
> 👨‍💻 : 강의 commit 지점

> 수업 전 사전작업
>
> `home/templates/index.html` 생성
>
> ```django
> {% extends 'base.html' %}
> {% block title %}Index{% endblock  %}
> {% block body %}
> 	<h1>저녁 장고!</h1>
>  	<a href="/home/dinner">저녁 추천 받기</a> d
> {% endblock  %}
> ```
>
> ```python
> def index(request):
>  	# return HttpResponse('Welcome to Django !')
>  	return render(request, 'index.html')
> ```

### 0. DTL

> Django Template Language
>
> [DTL](https://docs.djangoproject.com/en/2.1/ref/templates/language/)
>
> [공식문서 built-in](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)

> - views.py
>
> ```python
> from datetime import datetime
> 
> def template_example(request):
>  my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
>  my_sentence = 'Life is short, you need python'
>  messages = ['apple', 'banana', 'cucumber', 'mango']
>  datetimenow = datetime.now()
>  empty_list = []
>  return render(request, 'template_example.html', 
>            {'my_list': my_list, 'my_sentence': my_sentence, 'messages': messages, 'empty_list': empty_list, 'datetimenow': datetimenow})
> ```
>
> - urls.py
>
> ```python
> path('home/template_example/', views.template_example, name='template_example'),
> ```
>
> - template_example.html
>
> ```django
> <body style="height: 10000px;">
> </body>
> ```

1. `for`

   ```django
   <h3>1. 반복문</h3>
   {% for menu in my_list %}
   	<p>{{ menu }}</p>
   {% endfor %}
   <hr>
   ```

   ```django
   {% for menu in my_list %}
       {{ forloop.counter }}
       {% if forloop.first %}
           <p>짜장면+고추가루</p>
       {% else %}
           <p>{{ menu }}</p>
       {% endif %}
   {% endfor %}
   <hr>
   ```

   ```django
   {% for user in empty_list %}
       <p>{{ user }}</p>
   {% empty %}
       <p>지금 가입한 유저가 없습니다.</p>
   {% endfor %}
   <hr>
   ```

2. `if`

   ```django
   <h3>2. 조건문</h3>
   {% if '짜장면' in my_list %}
       <p>짜장면엔 고추가루지!!</p>
   {% endif %}
   ```

   ```django
   <p>3. length filter 활용</p>
   {% for message in messages %}
       {% if message|length > 5 %}
           <p>글씨가 너무 길어요.</p>
       {% else %}
           <p>{{ message }}, {{ message|length }}</p>
       {% endif %}
   {% endfor%}
   ```

   ```
   <=
   >=
   ==
   !=
   >
   <
   in
   not in
   is 
   모두 가능하다.
   ```

3. `lorem` (이미 정의되어 있는 변수 호출이기 때문에 `{% %}` 이다!)

   ```django
   <h3>4. lorem ipsum</h3>
   {% lorem %}
   <hr>
   {% lorem 3 w %}
   <hr>
   {% lorem 4 w random %}
   <hr>
   {% lorem 2 p %}
   ```

   * 기본 : 글씨
   * w : word 
   * p : `<p>` `</p>`, 문단
   * random : 무작위

   ```django
   <h3>5. 글자수 제한(truncate)</h3>
   <p>{{ my_sentence|truncatewords:3 }}</p>
   <p>{{ my_sentence|truncatechars:3 }}</p>
   <p>{{ my_sentence|truncatechars:10 }}</p>
   ```

   > chars는 `(공백)...` 즉, 4글자를 포함한 길이다.

4. 글자 관련 필터

   ```django
   <h3>6. 글자 관련 필터</h3>
   <p>{{ 'abc'|length }}</p>
   <p>{{ 'ABC'|lower }}</p>
   <p>{{ my_sentence|title }}</p>
   <p>{{ 'Abc def'|capfirst }}</p>
   <p>{{ my_list|random }}</p>
   ```

5. 연산

   ```django
   <h3>7. 연산</h3>
   <p>{{ 4|add:6 }}</p>
   ```

   > 더 많은 연산을 하려면,
   >
   > [django-mathfilters](https://github.com/dbrgn/django-mathfilters)

6. `now` : [참고 date filter](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#std:templatefilter-date)

   ```django
   <h3>8. 날짜표현</h3>
   {{ datetimenow }}<br>
   {% now "DATETIME_FORMAT" %}<br>
   {% now "SHORT_DATETIME_FORMAT" %}<br>
   {% now "DATE_FORMAT" %}<br>
   {% now "SHORT_DATE_FORMAT" %}
   <hr>
   {% now "Y년 m월 d일 (D) h:i" %}
   <hr>
   {% now "Y" as current_year %}
   	Copyright {{ current_year }}
   <hr>
   {{ datetimenow|date:"SHORT_DATE_FORMAT" }}
   ```

   * `DATETIME_FORMAT` `SHORT_DATETIME_FORMAT` `DATE_FORMAT` `SHORT_DATE_FORMAT`

7. 기타

   ```django
   <h3>9. 기타</h3>
   {{ 'google.com'|urlize }}
   ```

👨‍💻-"07_DTL Practice"

---
### 1. static 파일 관리

> **진행 중 적용이 안된다면 서버를 재시작 해보자.**
>
> `STATIC_URL = '/static/'` (setting.py 최하단에 있음)

1. views

   ```python
   def static_example(request):
       return render(request, 'static_example.html')
   ```

2. url

   ```python
   path('home/static_example/', views.static_example, name='static_example'),
   ```

3. template

   ```django
   {% extends "base.html" %}
   
   {% block body %}
       <img src="#" alt="audrey"></img>
   {% endblock %}
   ```

4. `home/static` 폴더 만들고 이미지 넣기

5. 정적파일 넣기(image)

   > **주의!! extends는 항상 최상단에 위치해 있어야 함.** 

   ```django
   {% extends "base.html" %}
   
   {% load static %}
   
   {% block body %}
       <img src="{% static 'audrey.png' %}" alt="audrey"></img>
   {% endblock %}
   ```

6. 정적파일 넣기(css)

   - base.html

     ```django
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <meta http-equiv="X-UA-Compatible" content="ie=edge">
         <title>{% block title %}{% endblock %}</title>
         {% block css %}{% endblock %}
     </head>
     ```

   - static_example.html

     ```django
     {% extends "base.html" %}
     
     {% load static %}
     
     {% block css %}
         <link rel="stylesheet" href="{% static 'style.css' %}" type="text/css" />
     {% endblock %}
     
     {% block body %}
         <img src="{% static 'audrey.png' %}" alt="audrey"></img>
     {% endblock %}
     ```

   - static/style.css

     ```css
     h1 {
         color: crimson;
     }
     ```

> 물론 static 안에 images, stylesheets 의 폴더로 더 구조화 가능. 다만 경로도 다시 바뀌어야 함 .`'images/audrey.png'`

👨‍💻-"08_Static URL"

---


### 2. URL 설정 분리

1. 두번째 app을 만들어봅시다. 

   ```bash
   $ python manage.py startapp utilities
   ```

2. 어떻게 해야할까?

   ```python
   from django.contrib import admin
   from django.urls import path
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('home/', views.index),
       path('home/lunch', views.lunch),
       path('home/hello/<name>/', views.hello),
   ]
   ```

   * 그런데 이제 import 를 하면 views 가 여러개가 된다.
   * **그래서 이제 앞으로 app마다 url 설정을 해야 한다.**

   ```python
   # home/urls.py
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('static_example/', views.static_example, name='static_example'),
       path('template_example/', views.template_example, name='template_example'),
       path('user_create/', views.user_create, name='user_create'),
       path('user_new/', views.user_new, name='user_new'),
       path('pong/', views.pong, name='pong'),
       path('ping/', views.ping, name='ping'),
       path('cube/<int:num>', views.cube, name='cube'),
       path('hello/<name>/', views.hello, name='hello'),
       path('dinner/', views.dinner, name='dinner'),
       path('index/', views.index, name='index'),
   ]
   ```

   ```python
   # django_intro/url.py
   from django.contrib import admin
   from django.urls import path, include # include 함수 import
   
   urlpatterns = [
       # 요청이 home/ 으로 오면, home/urls.py 에 설정들에 맞춰 뷰로 보내준다.
       path('home/', include('home.urls')),
       path('admin/', admin.site.urls),
   ]
   ```

   * 동일하게 동작하는지 최종 확인 !

   👨‍💻 - "09_ Separate URL multiple apps"

---

### 3. Template name spacing

1. utilities 기본 세팅 하기

   > ```python
   > # settings
   > 'utilities.apps.UtilitiesConfig',
   > 
   > # django_intro/urls.py
   > path('utilities/', include('utilities.urls')),
   > ```
   >
   > ```python
   > # utilities/urls.py
   > from django.urls import path
   > from . import views
   > 
   > urlpatterns = [
   >  	path('', views.index, name='index'),
   > ]
   > ```
   >
   > ```python
   > from django.shortcuts import render
   > 
   > # Create your views here.
   > def index(request):
   >  	return render(request, 'index.html')
   > ```
   >
   > ```django
   > <!DOCTYPE html>
   > ...
   > <body>
   >  	<h1>실습실습</h1>
   > </body>
   > </html>
   > ```

2. **그런데 유틸리티의 index 가 아닌 home 에서 설정된 index 의 모습이 나왔다. **
   **(장고가 바라보는 순서, template, static)**

3. `home/templates/home` & `home/static/home` 폴더 구조로 변경!

   1. home/views.py 안에 기존 템플릿 경로들 모두 수정 `example.html` --> `home/example.html`
   2. 그런데 base.html 때문에 템플릿 에러 발생 !

> static 파일도 마찬가지로 폴더 구조를 변경한다.
>
> `home/static/home/images/1.png`
>
> `home/static/home/stylesheet/style.css` 방식으로.

👨‍💻 - "10_ Separate Folders"

---

### 4. Template Inheritance

1. `base.html` 을 어디에 위치 시킬까?

   * app이 두개인데 어디에 넣을까?
   * root 에 넣자!
   * home 에 있던 base.html 를 아래 주소로 옮기자.

2. `django_intro/templates/base.html`

   ```django
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>{% block title %}{% endblock %}</title>
       {% block css %}{% endblock %}
   </head>
   <body>
       <h1>장고 연습</h1>
       <hr>
       {% block body %}
       {% endblock %}
   </body>
   </html>
   ```

3. `settings.py`

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   👨‍💻 - "11_ Template Inheritance_2"

---

### 5. 디렉토리 구조

이제 디렉토리 구조는 `home/templates/home/` 으로 구성된다.

디렉토리 설정은 `settings.py` 의 `TEMPLATES` 에 다음과 같이 되어 있다.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- `DIRS` : templates를 커스텀하여 경로를 설정할 수 있다.

  - 경로 설정

    ```python
    os.path.join(BASE_DIR, 'django_intro', 'templates')
    #=> PROJECT01/django_intro/templates
    ```

- `'APP_DIRS': True` : `INSTALLED_APPS` 에 설정된 app의 디렉토리에 있는 `templates` 를 템플릿으로 활용한다. 

- home 어플리케이션 최종 구조

  ```bash
  home
  ├── __init__.py
  ├── admin.py
  ├── apps.py
  ├── migrations
  ├── models.py
  ├── static
  │   └── home
  │       ├── images
  │       └── stylesheets
  ├── templates
  │   └── home
  ├── tests.py
  ├── urls.py
  └── views.py
  ```

