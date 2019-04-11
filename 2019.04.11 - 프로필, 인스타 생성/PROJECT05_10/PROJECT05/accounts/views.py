from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm # UserCreationForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout  # 뷰함수랑 이름이 같아서 바꿈
from django.contrib.auth import update_session_auth_hash   # 비밀번호 변경하려는 유저의 세션이 바뀌는 것 방지하는 모듈
from django.contrib.auth import get_user_model
from .forms import UserCustomChangeForm, UserCustomCreationForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:   # 로그인된 유저라면 바로 index로 보냄
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = UserCustomCreationForm(request.POST)   # user를 만드는 행위(CREATE)
        if form.is_valid():  # 유효성 검증
            user = form.save()
            auth_login(request, user)  # 회원가입과 동시에 로그인 됨
            return redirect('boards:index')
    else:
        form = UserCustomCreationForm()   # User를 만드는 form만 보여주면 된다
    context = {'form': form}
    # return render(request, 'accounts/signup.html', context)
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:   # 로그인된 유저라면 바로 index로 보냄
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())   # 유저 정보만 받아서 로그인함
            return redirect(request.POST.get('next') or 'boards:index')  # 둘 중의 하나 사이트로 이동
    else:    # next라는 변수를 받으면 redirect, next 변수가 없으면 index로 이동한다
        form = AuthenticationForm()
    context = {
            'form': form,
            'next': request.GET.get('next', ''),  # 키가 없으면 None이 아닌 빈 문자열을 넣는 것
    }
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)   # 세션 종료
    return redirect('boards:index')
    
    
def delete(request):  # 회원탈퇴 - 로그인된 상태만 가능
    user = request.user   # 유저 정보를 담아 지움
    if request.method == 'POST':
        user.delete()   # 유저가 삭제되면 자동으로 세션 종료됨
    return redirect('boards:index')  # method 방식에 상관없음
    
    
def edit(request):  # 회원 수정 홈페이지
    if request.method == 'POST':
        # 수정 로직 진행
        form = UserCustomChangeForm(request.POST, instance=request.user)   # POST 방식으로 유저의 정보를 받음
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    context = {'form': form}
    # return render(request, 'accounts/edit.html', context)
    return render(request, 'accounts/auth_form.html', context)
    

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)   # edit와 순서가 다르다(인자 순서 유의)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 현재 유저가 로그아웃 되는 것을 막는다
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form,}
    # return render(request, 'accounts/change_password.html', context)
    return render(request, 'accounts/auth_form.html', context)



def profile(request, user_pk):
    
    # board = get_object_or_404(Board, board_pk)
    # comment = get_object_or_404(Comment, comment_pk)
    
    # user - board
    # user - comment (모두 1:N이므로 나머지를 다 가져올 필요가 없다)
    
    user_info = get_object_or_404(get_user_model(), pk=user_pk)  # 헷갈릴까봐 이름을 바꿈
    
    context = {
        'user_info': user_info
    }
    return render(request, 'accounts/profile.html', context)
