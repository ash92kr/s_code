from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('articles:list')
    else:
        signup_form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'articles:list')
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})
    
def logout(request):
    auth_logout(request) 
    return redirect('articles:list')