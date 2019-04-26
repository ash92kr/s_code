from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    # Q1-1, Q1-2 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


# 주의
# 로그인 관련 함수가 보이지 않을 뿐 정상 로그인 됩니다.
# /accounts/login URL을 통해 로그인 됩니다.

def logout(request):
    auth_logout(request)
    return redirect("posts:list")