
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Hi there! Welcome to Cloud9 IDE!

To get you started, create some files, play with the terminal,
or visit http://docs.c9.io for our documentation.
If you want, you can also go watch some training videos at
http://www.youtube.com/user/c9ide.

Happy coding!
The Cloud9 IDE team



























































# posts - views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def list(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user   # 유저 정보 넣기
            post.save()
            return redirect('posts:detail', post.pk)   # 다시 넘겨줄 때는 _이 아니라 .!
    else:                                               # 위에서 post_pk를 정의하면 _ 사용 가능
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if request.user == post.user:
        if request.method == "POST":
            post.delete()
            return redirect('posts:list')
        else:
            return render('posts:detail', post_pk)
    else:
        return redirect('posts:list')


@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.user == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return render('posts:list')   # user 아니면 처음 페이지로 보내기
    context = {
        'form': form,
        'post': post,   # 이것도 보내야지
    }
    return render(request, 'posts/form.html', context)   # 어디로 전달할까?


@login_required
@require_POST
def comment_create(request, post_pk):
    # post = get_object_or_404(Post, pk=post_pk)
    
    form = CommentForm()
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id = request.user.id
        comment.post_id = post_pk
        comment.save()
        return redirect('posts:detail', post_pk)
        
@login_required
@require_POST
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('posts:detail', post_pk)


@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('posts:detail', post_pk)
        





























# posts - urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:post_pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.list, name='list'),
]



































# posts - forms.py
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="")   # albel 삭제
    class Meta:
        model = Comment
        fields = ['content',]





































# posts - list.html
{% extends 'base.html' %}

{% block body %}

    <h1>list</h1>

    <ul>
        {% for post in posts %}
            <p>작성자 : {{ post.user }}</p>
            <p></p><a href="{% url 'posts:detail' post.pk %}">{{ post.title }}</a></p>
            <hr>
        {% endfor %}
    </ul>
    
    <!--링크 분기-->
    {% if user.is_authenticated %}
        <a href="{% url 'posts:create' %}">글쓰기</a>
    {% else %}
        <a href="{% url 'accounts:login' %}">새 글을 쓰려면 로그인하세요.</a>
    {% endif %}

{% endblock %}




































# posts - detail.html
{% extends 'base.html' %}

{% block body %}

    <p>{{ post.pk }}번째 글</p>
    <p>{{ post.title }}</p>
    <p>{{ post.content }}</p>
    <hr>
    
    <a href="{% url 'posts:like' posk.pk %}">
        {% if user in post.like_users.all %}
                안 좋아요
        {% else %}
                좋아요
        {% endif %}
    </a>
    <p>{{ post.like_users.count }}명이 좋아합니다.</p>

    {% for comment in post.comment_set.all %}
        
        {{ comment.user }}
        {{ comment.content }}
        {% if user == post.user %}  <!--현재 user인지 아닌지 파악-->
            <form action="{% url 'posts:comment_delete' post.pk comment.pk %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="Submit"/>
            </form>
        {% endif %}

    {% empty %}
            <p>댓글이 없습니다.</p>
    {% endfor %}
    
    
    {% if user.is_authenticated %}
        <form action="{% url 'posts:comment_create' post.pk %}" method="POST">
            {% csrf_token %}
            {{ comment_form.as_p }}
            <input type="submit" value="Submit"/>
        </form>
    {% else %}
        <a href="{% url 'accoutns:login' %}">댓글을 작성하려면 로그인하세요.</a>
    {% endif %}

    <a href="{% url 'posts:list' %}">BACK</a>
    <a href="{% url 'posts:update' post.pk %}">수정</a>

{% endblock %}











































# accounts - views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # 회원가입, 로그인 폼

# Create your views here.
def signup(request):
    
    if request.user.is_authenticated:   # 로그인된 상태면 회원가입 불가
        return redirect('posts:list')
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)   # 회원가입시 자동 로그인 전환
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)   # 인자가 2개 들어간다
        if form.is_valid():
            auth_login(request, form.get_user())  # form.get_user() 외우기
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
    
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')































# accounts - signup.html, login.html
{% extends 'base.html' %}

{% block body %}

    <h1>회원가입</h1>
    
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit"/>
    </form>

{% endblock %}












