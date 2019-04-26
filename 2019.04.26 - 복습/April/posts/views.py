from django.shortcuts import render, redirect
# 4-1번 문제의 답안 코드
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})

@login_required
def create(request):
    # Q2-2, Q2-3 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:list')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)
        
        
@login_required
def like(request, post_id):
    # Q3-1 문제의 답안 코드를 pass를 지우고 아래에 작성하세요.
    post = Post.objects.get(id=post_id)
    
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    
    return redirect('posts:list')