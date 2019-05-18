from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)   # 제출 버튼 자체??
        if form.is_valid():
            post = form.save()   # 이 부분은 가능한 변수로 넣기
            return redirect('posts:detail', post.pk)   # 넘길 때는 .pk로 넘겨야 한다 -> 그리고 comment를 추가해야 한다
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

    
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')   # 삭제하면 delete로 되돌아갈 수 없다


def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()   # 저장한 form에는 pk가 있다
            return redirect('posts:detail', post.pk)  # 다시 한 번 넘겨줄 때는 .을 적어야 한다
    else:
        form = PostForm(instance=post)   # GET 방식이면 기존에 입력한 내용을 instance에 넘겨주어야 한다
    context = {
        'form' : form,
    }
    return render(request, 'posts/form.html', context)  # form.html로 redirect하기




