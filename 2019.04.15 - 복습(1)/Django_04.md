## Django_04

**Content**

0. Detail
1. Delete
2. Update

> 190221 Thu

---

### 0. detail

```python
# views.py
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {'board': board})
```

```python
# boards/urls.py
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]   
```

```django
<!-- boards/detail.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Detail</h1>
    <h2>{{ board.id }} 번째 글</h2>
    <hr>
    <h2>{{ board.title }}</h2>
    <p>{{ board.content }}</p>
    <p>{{ board.created_at }}</p>
    <p>{{ board.updated_at }}</p>
    <a href="/boards/">Back</a>
{% endblock %}
```

```django
<!-- boards/index.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="/boards/new">글 작성하기</a>
    <hr>
    {% for board in boards %}
        <p>{{ board.id }}</p>
        <p>{{ board.title }}</p>
        <p>{{ board.created_at|timesince }}전</p>
        <a href="/boards/{{ board.pk }}/">[글 보러가기]</a>
    <hr>
    {% endfor %}
{% endblock %}
```

---

### 1. Delete

```python
# views.py
from django.shortcuts import render, redirect

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board(title=title, content=content)
    board.save()
    return redirect(f'/boards/{board.pk}/')

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')
```

```python
# boards/urls.py
urlpatterns = [
    path('<int:pk>/delete/', views.delete, name='delete'),
]  
```

```django
<!-- boards/index.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="/boards/new">글 작성하기</a>
    <hr>
    {% for board in boards %}
        <p>{{ board.id }}</p>
        <p>{{ board.title }}</p>
        <p>{{ board.created_at|timesince }}전</p>
        <a href="/boards/{{ board.pk }}/">[글 보러가기]</a>
        <a href="/boards/{{ board.pk }}/delete/" onclick="return confirm('R U SURE?')">[삭제]</a>
    <hr>
    {% endfor %}
{% endblock %}
```

---

### 2. Update

- edit

```django
<!-- boards/index.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>Board</h1>
    <a href="/boards/new">글 작성하기</a>
    <hr>
    {% for board in boards %}
        <p>{{ board.id }}</p>
        <p>{{ board.title }}</p>
        <p>{{ board.created_at|timesince }}전</p>
        <a href="/boards/{{ board.pk }}/">[글 보러가기]</a>
        <a href="/boards/{{ board.pk }}/delete/" onclick="return confirm('R U SURE?')">[삭제]</a>
        <a href="/boards/{{ board.pk }}/edit/">[수정]</a>
    <hr>
    {% endfor %}
{% endblock %}
```

```python
# views.py
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board': board})
```

```python
# boards/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/edit/', views.edit, name='edit'),
]   
```

```django
<!-- boards/edit.html -->
{% extends 'boards/base.html' %}
{% block body %}
    <h1>EDIT</h1>
    <form action="/boards/{{ board.pk }}/update/" method="POST">
        {% csrf_token %}
        <label for="title">Title</label>
        <input type="text" name="title" id="title" value="{{ board.title }}"/><br>
        <label for="content">Content</label>
        <textarea name="content" id="content">{{ board.content }}</textarea>
        <input type="submit" value="Submit"/>
    </form>
    <a href="/boards/">BACK</a>
{% endblock %}
```

- update

```python
# views.py
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}/')
```

```python
# boards/urls.py
urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),
]   
```













