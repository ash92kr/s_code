# 2019.02.13 workshop



1. 이름이 first_workshop 프로젝트 생성

```bash
mkdir homeworkshop
cd homeworkshop
pyenv local django-venv
django-admin startproject first_workshop .
```



2. https://~~~/info의 경로로 들어갔을 때 반 정보를 보여주는 페이지 만들기

```python
# (1) settings.py 설정 - 로켓 보이기
ALLOWED_HOSTS = ['django-intro-sanghyeon2.c9users.io']
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```



```bash
# (2) 앱 만들기
python manage.py startapp student
```



```python
# (3) 앱 환경설정하기
INSTALLED_APPS = [
    'student.apps.StudentConfig',
]
```



```python
# (4-1) view 만들기
from django.shortcuts import render

def info(request):
    return render(request, 'info.html')   # info.html 불러오기
```



```python
# (4-2) url 설정하기
from django.contrib import admin
from django.urls import path
from student import views   # student의 views 파일을 import하기

urlpatterns = [
    path('student/info/', views.info, name='info'),   # student/info/ url 설정, info 뷰함수 생성
    path('admin/', admin.site.urls),
]
```



```django
<!--(4-3) template 만들기-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Info</title>
</head>
<body>
    <h1>우리반 정보</h1>
    
    <h3>Teacher</h3>
    <ul>
        <li>NAME</li>
    </ul>
    
    <h3>Student</h3>
    <ul>
        <li>홍길동</li>
        <li>김길동</li>
        <li>박길동</li>
    </ul>
    
</body>
</html>
```



3. https:// ~~~/student/<학생이름>의 경로로 들어갔을 때 학생의 이름과 나이를 보여주는 페이지 만들기

```python
# (1) views.py(뷰 생성)
def student(request, name):

	# dictionary 생성
    work = {
        '성연혁': 20,
        '최운우': 25,
        '김윤중': 23,
        '최비선': 22,
        '진순옥': 24,
        '천정은': 21
    }
    
    return render(request, 'student.html', {'name': name, 'age': work[name]})
```



```python
# (2) urls.py(url 설정)
    path('student/student/<name>', views.student, name='student'),
```



```django
<!--(3) student.html(template 생성)-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Student</title>
</head>
<body>
    <h1>이름 : {{ name }}</h1>
    <h2>나이 : {{ age }}</h2>
</body>
</html>
```

