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
        
