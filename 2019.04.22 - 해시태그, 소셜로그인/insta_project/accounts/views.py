from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm  # User 모델을 가지고 있는 모델폼
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm, CustomUserChangeForm
from .models import Profile

# Create your views here.
def signup(request):
    if request.user.is_authenticated:   # 현재 유저가 로그인 상태인지 판단
        return redirect('posts:list')   # 회원가입한 정보로 바로 로그인되도록 함
    
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)   # 회원가입 후 바로 로그인 상태로 만들기
            return redirect('posts:list')
    else:
        # form = UserCreationForm()
        form = CustomUserChangeForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
    

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # return redirect('posts:list')
            return redirect(request.GET.get('next') or 'posts:list')
            # 비로그인 상태면 posts/create이나 posts/update를 입력해도
            # next 뒤에 있는 /accounts/login/?next=/posts/create/ 주소로 이동함
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)  # 기본 redirect 경로가 accounts/login으로 설정됨
    

def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    

def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    context = {
        'people': people,
    }
    return render(request, 'accounts/people.html', context)


# @login_required
# def update(request):
#     if request.method == 'POST':
#         pass
#     else:
#         user_change_form = CustomUserChangeForm(instance=request.user)
#     context = {
#         'user_change_form': user_change_form,
#     }
#     return render(request, 'accounts/update.html', context)
    
    
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)   # 그 사람이 입력한 내용을 기본으로 줌
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people', request.user.username)   # 그 사람의 profile로 이동
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)  # 기본 폼
    context = {
        'user_change_form': user_change_form,
    }
    return render(request, 'accounts/update.html', context)
    

@login_required
def delete(request):
    if request.method == "POST":
        request.user.delete()
    return redirect('posts:list')


@login_required
def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
    context = {
        'password_change_form': password_change_form,
    }
    return render(request, 'accounts/password.html', context)
    
    
@login_required
def profile_update(request):
    profile = Profile.objects.get_or_create(user=request.user)  # 카카오 계정은 object가 없어 없으면 create, 있으면 get을 취한다  
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'accounts/profile_update.html', context)
    

@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)

        