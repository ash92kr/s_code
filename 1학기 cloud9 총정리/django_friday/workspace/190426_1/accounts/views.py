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

