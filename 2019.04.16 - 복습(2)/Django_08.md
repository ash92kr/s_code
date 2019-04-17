[TOC]

## Django_08

**Content**

0. Forms
1. ModelForm
2. Bootstrap ModelForm

> 190321 Thu

---

### 0. Forms

> [Forms](https://docs.djangoproject.com/en/2.1/ref/forms/#forms)
>
> [MDN 폼(form)으로 작업하기](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms)

- 우리는 지금까지 html form tag 를 직접 사용하면서 사용자로부터 데이터를 받았다.
- 이렇게 직접 사용하면 각 html 에 일일이 코드를 작성해야하고, field 가 많다면 불필요한 반복이 계속 될 것이다.
- 그래서 form tag 를 django 에서 지원하는 Class 로 만들어서 재사용 가능한 코드를 작성해보자.
- 먼저 기존방식대로 form tag 로 작성해보고, Class 구조로 변경해보자.

#### 0.1 Start Project & App

```bash
$ mkdir PROJECT04
$ cd PROJECT04
$ pyenv virtualenv 3.6.7 form-venv 
$ pyenv local form-venv

$ pip install django
$ django-admin startproject myform .
$ python manage.py startapp boards
```

- settings.py 설정 / gitignore 설정

  ```python
  ALLOWED_HOSTS = ['*']
  
  INSTALLED_APPS = [
      'boards.apps.BoardsConfig',
      ...
  ]
  
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  
  USE_TZ = False
  ```

  > 로켓 페이지 확인하기


#### 0.2 Board Model

```python
# boards/models.py
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

>- admin 설정 (관리자 계정 만들고 모델 문제 없는지 확인)
>
>```python
>from django.contrib import admin
>from .models import Board
>
># Register your models here.
>class BoardAdmin(admin.ModelAdmin):
>    list_display = ('title', 'content', 'created_at', 'updated_at',)
>admin.site.register(Board, BoardAdmin)
>```
>
>- url 설정
>
>```python
># myform/urls.py
>
>from django.contrib import admin
>from django.urls import path, include
>
>urlpatterns = [
>    path('boards/', include('boards.urls')),
>    path('admin/', admin.site.urls),
>]
>```

#### 0.3 Create (with html form)

> [Using a model formset in a view](https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/#using-a-model-formset-in-a-view)

> - index 페이지 만들기
>
> ```python
> from .models import Board
> 
> def index(request):
>      boards = Board.objects.order_by('-pk')
>      context = {'boards': boards}
>      return render(request, 'boards/index.html', context)
> ```
>
> ```python
> from django.urls import path
> from . import views
> 
> app_name = 'boards'
> 
> urlpatterns = [
>      path('', views.index, name='index'),
> ]
> ```
>
> ```django
> <!-- boards/base.html 부트스트랩 없이 -->
> <body>
>       {% block body %}
>       {% endblock %}
> </body>
> ```
>
> ```django
> <!-- boards/index.html -->
> {% extends 'boards/base.html' %}
> {% block body %}
> <h1>게시글 목록</h1>
> {% for board in boards %}
> 	<p>{{ board.pk }}</p>
> 	<p>{{ board.title }}</p>
> 	<hr>
> {% endfor %}
> {% endblock %}
> ```

- **Create**

  ```python
  # views.py
  from django.shortcuts import render, redirect
  
  def create(request):
      if request.method == 'POST':
          title = request.POST.get('title')
          content = request.POST.get('content')
          board = Board(title=title, content=content)
          board.save()
          return redirect('boards:index')
      else:
          return render(request, 'boards/create.html')
  ```

  ```python
  # boards/urls.py
  path('new/', views.create, name='create'),
  ```

  ```django
  <!-- boards/create.html -->
  {% extends 'boards/base.html' %}
  {% block body %}
  <h1>NEW board</h1>
  <form method="POST">
    	{% csrf_token %}
      <label for="title">Title</label>
      <input type="text" name="title" id="title"><br>
      <label for="content">Content</label>
      <textarea name="content" id="content"></textarea>
      <input type="submit" value="submit">
  </form>
  {% endblock %}
  
  
  <!-- boards/index.html -->
  <h1>게시글 목록</h1>
  <a href="{% url 'boards:create' %}">새 글 작성</a>
  ```

- **Detail**

  ```python
  # views.py
  def detail(request, board_pk):
      board = Board.objects.get(pk=board_pk)
      context = {'board': board}
      return render(request, 'boards/detail.html', context)
  ```

  ```python
  # boards/urls.py
  path('<int:board_pk>/', views.detail, name='detail'),
  ```

  ```django
  <!-- boards/detail.html -->
  {% extends 'boards/base.html' %}
  {% block body %}
  <h1>{{ board.pk }}번째 글</h1>
  <h2>{{ board.title }}</h2>
  <hr>
  <p>{{ board.content }}</p>
  <a href="{% url 'boards:index' %}">BACK</a>
  {% endblock %}
  
  
  <!-- boards/index.html -->
  {% for board in boards %}
  	..
  	<a href="{% url 'boards:detail' board.pk %}">글 보러가기</a>
  	<hr>
  {% endfor %}
  ```

  > CR 로직이 잘 동작하는지 확인 !

#### 0.4 Create (with Form Class)

> [The Forms API](https://docs.djangoproject.com/en/2.1/ref/forms/api/#module-django.forms)
>
> [Form fields](https://docs.djangoproject.com/en/2.1/ref/forms/fields/#module-django.forms.fields)
>
> [Widgets](https://docs.djangoproject.com/en/2.0/ref/forms/widgets/#module-django.forms.widgets)
>
> `Form` 을 선언하는 문법은 `Model`을 선언하는 것과 많이 닮았으며, 같은 필드타입을 사용한다. (또한 일부 매개변수도 유사하다) . 두가지 경우 모두 각 필드가 데이타에 맞는 (유효성 규칙에 맞춘) 타입인지 확인할 필요가 있고, 각 필드가 보여주고 문서화할 description을 가진다는 것에서 Form과 Model이 유사한 문법으로 구성된다는 점을 납득할 수 있다. 

- **Form 선언** - boards app 폴더에 `forms.py` 를 만든다. 

  > cleaned_data 한 다음에 다시 돌아오기

  ```python
  # forms.py
  from django import forms 
  
  class BoardForm(forms.Form): 
      title = forms.CharField()
      # title = forms.CharField(max_length=10)
      content = forms.CharField()
  ```

- widget 인자의 속성을 통해서 어떤 tag 를 사용할지, 기타 속성 등도 지정할 수 있다.

  ```python
  # forms.py
  from django import forms 
  from .models import board
  
  class BoardForm(forms.Form): 
      title = forms.CharField(label='제목', 
                              widget=forms.TextInput(attrs={ 
                                  'placeholder': 'The title!',
                              }),
                              error_messages={'required': 'Please enter the Title'} 
                              )
      content = forms.CharField(label='내용', 
                                widget=forms.Textarea(attrs={ 
                                  'class': 'input-content', 
                                  'rows': 5, 
                                  'cols': 50, 
                                  'placeholder': 'Fill the Content!', 
      	                    }))
  ```

  > **필드 공통 인자** 
  >
  > - required : 기본으로 True  빈 칸을 허용하기 위해서는 `required=False`
  >
  > - label : HTML 필드를 렌더링할 때 사용하는 레이블 (자동으로 Title으로 잡아줌)
  >
  > - label_suffix : 기본으로 콜론이 지정된다.
  >
  > - Initial : 필드 초기값
  >
  > - widget : 디스플레이 위젯.
  >
  > - Help_text : 필드 사용법 보여줌
  >
  > - Error_messages : 에러메세지 목록, 문구 수정가능 
  >
  >   ```python
  >   name = forms.CharField(error_messages={'required': 'Please enter your name'})
  >   ```
  >
  >   ```
  >   CharField :  
  >   	required, max_length, min_length
  >   
  >   DateField : 
  >   	required, invalid
  >   
  >   DateTimeField : 
  >   	required, invalid
  >   
  >   ImageField : 
  >   	required, invalid, missing, empty, max_length
  >   
  >   IntegerField : 
  >   	required, invalid, max_value, min_valued (%(limit_value)s)
  >   ```
  >
  > - Disabled / localize / validators

- **cleaned_data**

  > `cleaned_data`
  >
  > - 기본 유효성 검사도구를 이용해 입력값을 "다듬고(cleaned)" 잠재적으로 안전하지 않을 수 있는 입력 값을 정화하며 , 해당 입력값에 맞는 표준 형식으로 변환해준다.
  > - 깔끔한 데이타(cleaned_data)란 것은  정제되고(sanitised), 유효성체크가되고, 파이썬에서 많이쓰는 타입의 데이타이다.

  ```python
  # views.py
  from .forms import BoardForm
  
  def create(request):
      # POST 요청이면 폼 데이터를 처리한다
      if request.method == 'POST':
          # 이 처리과정은 "binding"으로 불리며 폼의 유효성 체크를 할수 있도록 해준다.
          form = BoardForm(request.POST) 
          # form 유효성 체크 (form 이 유효한지 체크한다)
          if form.is_valid():
              title = form.cleaned_data.get('title')
              content = form.cleaned_data.get('content')
              # 검증을 통과한 깨끗한 데이터를 form 에서 가져와서 board 을 만든다.
              board = Board.objects.create(title=title, content=content)
              return redirect('boards:detail', board.pk)
      # GET 요청 (혹은 다른 메소드)이면 기본 폼을 생성한다. 
      else:
          form = BoardForm()
      context = {'form': form}
      return render(request, 'boards/create.html', context)
  ```

  ```django
  <!-- boards/create.html --> 
  <h1>New board</h1> 
  <form method="POST"> 
      {% csrf_token %} 
      {{ form.as_p }} 
      <input type="submit" value="Submit"> 
  </form>
  ```

  - **input, textarea 같은 tag 들이 모두 form 안으로 들어갔다.**
  - `as_p` 는 ""각 input tag 를 p tag 로 렌더링(감싸겠다)하겠다" 는 뜻이다. (`as_table`, `as_ul` 도 있다.)

- Form Class 의 장점 (자동으로 해주는 것들)
  - `models.py`에서 `blank=True`  와 같은 빈 값을 허용하는 옵션을 주지 않았다면, 자동으로 input tag 에 `required` 가 추가되어 생성된다. (직접 input tag 를 만들때는 일일이 넣어주어야 했다. 안 넣은 상태에서 빈 값을 입력하게 되면 에러 페이지가 나오곤 했다.)
  - 입력된 값이 유효하지 않은 경우(예를들어 길이 제한을 넘었거나 하는 경우에) 에러 페이지를 띄우는 것이 아니라 에러 메세지를 form 이 있는 페이지에 자동으로 보여준다.
    - 이것이 동작하는 원리는 `is_valid()` 를 통과하지 못해 다시 `return render()` 를 실행하게 되기 때문이다.
    - 다만 `new/` 페이지와 다른 점은 `boardForm(request.POST)` 로 사용자가 입력한 값이 미리 설정되게 된다는 점이다.

#### 0.5 get_object_or_404

- 해당 객체가 있다면 `objects.get(pk=board_pk)` 을 실행하고 없다면 404 에러를 사용자에게 보낸다.

> https://docs.djangoproject.com/en/2.1/topics/http/shortcuts/#get-object-or-404
>
>  url 에서 없는 게시글 번호로 들어가서 서버 500 에러를 확인해보자.

```PYTHON
# boards/views.py
from django.shortcuts import render, redirect, get_object_or_404

def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)
```

#### 0.6 Delete

```python
# boards/views.py
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else: 
        return redirect('boards:detail', board.pk)
```

```python
path('<int:board_pk>/delete/', views.delete, name='delete'),
```

```django
<!-- boards/detail.html -->
<form action="{% url 'boards:delete' board.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
</form>
```

#### 0.7 Update

- `create.html` 템플릿을 그대로 사용하기 때문에 따로 템플릿을 만들지 않는다.

```python
# boards/views.py
def update(request, board_pk):
    # 1. board_pk 에 해당하는 오브젝트를 가져온다.
    # - 없으면 404 에러 // 있으면 board = Board.objects.get() 와 동일
    board = get_object_or_404(Board, pk=board_pk)
    # 2-1. POST 요청이면 (사용자가 form을 통해 데이터를 보내준 것)
    if request.method == 'POST':
      	# 사용자 입력값(request.POST)을 form 에 전달해주고
        form = BoardForm(request.POST)
        # 검증(유효성체크)
        if form.is_valid():
            board.title = form.cleaned_data.get('title')
            board.content = form.cleaned_data.get('content')
            board.save()
            return redirect('boards:detail', board.pk)
    # 2-2. GET 요청이면 (수정하기 버튼을 눌렀을 때))
    else:  
      	# BoardForm 을 초기화(사용자 입력값을 넣어준 상태)
        form = BoardForm(initial=board.__dict__)
		# context 에 담겨있는 form 은
    # 1. POST : 요청에서 검증에 실패하였을때, 오류 메세지가 포함된 상태
    # 2. GET : 요청에서 초기화된 상태
    context = {'form': form}
    return render(request, 'boards/create.html', context)
```

```python
# 주석을 제거한 코드
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data.get('title')
            board.content = form.cleaned_data.get('content')
            board.save()
            return redirect('boards:detail', board.pk)
    else:  
      # form = BoardForm(initial={'title': board.title, 'content': board.content})
        form = BoardForm(initial=board.__dict__)
    context = {'form': form}
    return render(request, 'boards/create.html', context)
```

```python
path('<int:board_pk>/edit/', views.update, name='update'),
```

```django
<!-- boards/detail.html -->
<a href="{% url 'boards:update' board.pk %}">수정</a>
```

> 그런데 template 은 깔끔해졌지만 view 의 모습은 예전과 비슷하다.

---

### 1. ModelForm

> [Creating forms from models](https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/#module-django.forms.models)
>
> [MDN: ModelForms](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms#ModelForms)

- 앞선 FormClass 에서는 Model 에서 이미 정의한 필드를 반복해서 정의했다.

- 하지만 지금처럼 Model 에 이미 필드를 정의했기 때문에 다시 필드 유형을 정의하는 것을 불필요하다.

- 이러한 이유로 django 는 django model 을 통해 Form class 를 만들 수 있는 helper(도우미)를 제공한다.

  - 즉, form 에서 모델 정의를 다시 작성하는 대신 ModelForm helper 클래스를 사용하여 모델에서 form을 작성하는 것이 더 쉽다.
  - 그런 다음 ModelForm은 일반 Form 과 완전히 같은 방식으로 view 내에서 사용할 수 있다.

- 아래 코드를 작성하고 new 페이지 변화 먼저 확인하기 (자동으로 모델 필드에 맞춰서 input 태그 생성해준다)

  ```python
  from django import forms 
  from .models import Board
  
  # class BoardForm(forms.Form): 
  #     title = forms.CharField(label='제목', 
  #                             widget=forms.TextInput(attrs={ 
  #                                 'placeholder': 'The title!',
  #                             }),
  #                             error_messages={'required': 'Please enter the Title'} 
  #                             )
  #     content = forms.CharField(label='내용', 
  #                               widget=forms.Textarea(attrs={ 
  #                                 'class': 'input-content', 
  #                                 'rows': 5, 
  #                                 'cols': 50, 
  #                                 'placeholder': 'Fill the Content!', 
  #     	                    }))
  
  class BoardForm(forms.ModelForm):
      class Meta: 
          model = Board 
          fields = ['title', 'content',]  # fields = '__all__' 
  ```

```python
# forms.py
from django import forms
from .models import board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={
                                            'placeholder': '제목을 입력해주세요.',
                                            'class': 'title'}),
                   'content': forms.Textarea(attrs={
                                            'class': 'content-input', 
                                            'rows': 5, 
                                            'cols': 50, 
                                            'placeholder': 'HI THERE?', })}
        error_messages = {'title': {
                                    'required': '제목을 반드시 입력해주세요.'
                                    },
                          'content': {
                                    'required': '내용을 반드시 입력해주세요.'
                                    },
                         } 
```

- 기존 BoardForm 클래스를 주석처리하고, 같은 이름의 새로운 클래스를 만든다.
  - **기존 class 와 다르게 `ModelForm` 을 상속받는다.**
  - Model 정보를 받아, 해당 Model 이 가지고 있는 field 에 맞춰 input 을 자동으로 만들어준다.
- `class Meta` 는 Model 의 정보를 작성하는 곳이다. 
- `fields` 를 작성하면, models.py 에 지정해놓은 CharField, TextField 등을 사용한다.

#### 1.1 Create

```python
# views.py
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/create.html', context)
```

> create 가 잘 동작하는지 확인해보자.

#### 1.2 Update

- ModelForm class 는 update 로직에서 진가가 드러난다.

  ```python
  # views.py
  def update(request, board_pk):
      board = get_object_or_404(Board, pk=board_pk)
      if request.method == 'POST':
          form = BoardForm(request.POST, instance=board) # 1
          if form.is_valid():
              board = form.save() # 2
              return redirect('boards:detail', board.pk)
      else:
          form = BoardForm(instance=board) # 3
      context = {'form': form}
      return render(request, 'boards/create.html', context)
  ```

  - create 와 다른점은 기존의 데이터를 가져와 수정하는 것이다.
    - `board` 을 DB 에서 가져와서, BoardForm 에 인스턴스 설정을 `instance=board` 로 설정해준다.

- create.html

  - 기존 템플릿을 그대로 사용하고 있다.

  - 우리가 아는 수정페이지에서는 input tag 를 field 개수만큼 만들어서 value 에 값을 일일이 넣었을 것이다.

  - 하지만 Form class 는 알아서 다 해준다.

    > create.html 은 create 페이지가 아닌 update 에서도 사용되니까, `form.html` 로 이름을 바꿔보자.

  ```python
  # views 에서 create.html 을 모두 form.html 로 바꾼다.
  return render(request, 'boards/form.html', {'form': form}
  ```

- *[부록]* form.py 의 위치

  - Form class 는 아래처럼 models.py 에도 작성할 수 있고 다른 위치 어느 곳에 두어도 상관은 없다.
  - 하지만, **Form class 는 form.py 에 작성하는 것이 관례**다.

  ```python
  # models.py
  from django.db import models
  from django import forms 
  
  class board(models.Model):
  		...
  
  class boardForm(forms.ModelForm):
      class Meta: 
          model = board 
          fields = ['title', 'content',] 
  		...
  ```

#### 1.3 추가사항

> https://stackoverflow.com/questions/792410/django-how-can-i-identify-the-calling-view-from-a-template

- 현재 새 글 작성, 기존 글 수정 시 `form.html` 에는 항상 NEW board 이라는 문구만 나온다.
- `request.resolver_match.url_name` 를 통해 현재 페이지의 url name 을 찾을 수 있는데, 이것을 이용해서 수정할 때와 새 글을 쓸 때 다르게 출력시켜 보자.

```django
<!-- boards/form.html -->
{% if request.resolver_match.url_name == 'create' %}
    <h1>NEW board</h1>
{% else %}
    <h1>EDIT board</h1>
{% endif %}
```

- 또한 새 글 작성에서 뒤로가는 버튼과 기존 글 수정에서 뒤로가는 버튼은 동작이 달라야 한다.

```django
<!-- boards/form.html -->
{% if request.resolver_match.url_name == 'create' %}
    <a href="{% url 'boards:index' %}">BACK</a>
{% else %}
    <a href="{% url 'boards:detail' board.pk %}">BACK</a>
{% endif %}
```

```python
# boards/views.py
    else:  
        form = BoardForm(instance=board)
    context = {
        'form': form,
        'board': board,
        }
```

---

### 2. Bootstrap ModelForm

> [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)

```bash
$ pip install django-crispy-forms
$ pip freeze > requirements.txt		# 프로젝트 중간 점검
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

- CDN 등록(base.html) 후 form.html 를 아래와 같이 변경

  ```django
  {% extends 'boards/base.html' %}
  {% block body %}
  {% load crispy_forms_tags %}
  
  ...
  
  <form method="POST">
    	{% csrf_token %}
      {{ form|crispy }}
      <input type="submit" value="submit">
  </form>
  {% endblock %}
  ```

#### 2.1 form 쪼개기

> [Rendering fields manually](https://docs.djangoproject.com/en/2.0/topics/forms/#rendering-fields-manually)

- template 에서 `{{ form }}`  으로 한번에 사용해서 커스터마이징이 힘들었는데, 쪼개서 사용도 가능하다.

- 굉장히 세부적으로 쪼갤 수 있지만, 간단하게 label, input, error 정도만 나눠보자.

  - errors: ul, li tag 로 표시
  - label_tag: label tag 로 표시
  - input: input_tag 로 표시

  ```django
  <!-- boards/form.html -->
  <h1>New board</h1> 
  
  {{ form.non_field_errors }}
  <form method="POST">
      {% csrf_token %}
      <div>
          {{ form.title.errors }}
          {{ form.title.label_tag }}
          {{ form.title }}
      </div>
      <div>
          {{ form.content.errors }}
          {{ form.content.label_tag }}
          {{ form.content }}
      </div>
      <input type="submit" value="submit">
  </form>
  
  --------
  
  <form method="POST">
    	{% csrf_token %}
    	<div class="row">
        	{% for field in  form %}
            	<div class=col-6>
                  {{ field.errors }}
                  {{ field.label_tag }} {{ field }}
              </div>
          {% endfor %}
      </div>
      <input type="submit" value="submit">
  </form>
  
  --------
  
  <form method="POST">
      {% csrf_token %}
      <div class="row">
          <div class="col-6">
              {{ form.title }}
          </div>
          <div class="col-10">
              {{ form.content }}
          </div>
          <input type="submit" value="submit">
      </div>
  </form>
  ```

#### 2.2 FormHelper

> [FormHelper API](https://django-crispy-forms.readthedocs.io/en/latest/api_helpers.html?highlight=helper#module-helper)

```python
# forms.py
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BoardForm(forms.ModelForm):
	class Meta:
    
    ...
    
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.form_method = 'POST'
      self.helper.add_input(Submit('submit', '작성!'))
```

```django
<!-- boards/form.html -->
{% extends 'boards/base.html' %}
{% load crispy_forms_tags %}
{% block body %}

{% crispy form %}

{% endblock %}
```

> csrf_token, submit, input 등 기본 form 형식을 `{% crispy form %}` 한줄로 작성해 줄 수 있다.

