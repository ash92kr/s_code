from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout  # 뷰함수랑 이름이 같아서 바꿈

# Create your views here.
def signup(request):
    if request.user.is_authenticated:   # 로그인된 유저라면 바로 index로 보냄
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)   # user를 만드는 행위(CREATE)
        if form.is_valid():  # 유효성 검증
            user = form.save()
            auth_login(request, user)  # 회원가입과 동시에 로그인 됨
            return redirect('boards:index')
    else:
        form = UserCreationForm()   # User를 만드는 form만 보여주면 된다
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:   # 로그인된 유저라면 바로 index로 보냄
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('boards:index')
    