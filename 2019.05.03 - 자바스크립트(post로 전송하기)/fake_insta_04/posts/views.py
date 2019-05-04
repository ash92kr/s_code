from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from itertools import chain
from django.db.models import Q
from .forms import PostForm, ImageForm, CommentForm
from .models import Post, Image, Comment, Hashtag

# Create your views here.
@login_required
def list(request):
    # 1
    followings = request.user.followings.all()
    posts = Post.objects.filter(Q(user__in=followings) | Q(user=request.user.id)).order_by('-pk')
    
    # 2
    # followings = request.user.followings.all()
    # chain_followings = chain(followings, [request.user])
    # posts = Post.objects.filter(user__in=chain_followings).order_by('-pk')

    # etc
    # posts = Post.objects.filter(user__in=request.user.followings.all()).select_related('user').prefetch_related('like_users').order_by('-pk')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        }
    return render(request, 'posts/list.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            # hashtag - 1
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag, new = Hashtag.objects.get_or_create(content=word)
                    if new:
                        post.hashtags.add(hashtag)
            # hashtag - 2
            # for word in post.content.split():
            #     if word.startswith('#'):
            #         hashtag = Hashtag.objects.get_or_create(content=word)
            #         post.hashtags.add(hashtag[0])
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {
        'post_form': post_form,
        'image_form': ImageForm,
        }
    return render(request, 'posts/form.html', context)

@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            # hashtag
            post.hashtags.clear()
            for word in post.content.split():
                if word.startswith('#'):
                    hashtag, new = Hashtag.objects.get_or_create(content=word)
                    if new:
                        post.hashtags.add(hashtag)
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form,}
    return render(request, 'posts/form.html', context)

def delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user != request.user:
        return redirect('posts:list')

    if request.method == 'POST':
        post.delete()
    return redirect('posts:list')

@require_POST
@login_required
def comment_create(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_pk
        comment.save()
    return redirect('posts:list')

@require_POST
@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')

@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:list')

@login_required
def explore(request):
    posts = Post.objects.order_by('-pk')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        }
    return render(request, 'posts/explore.html', context)

@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    posts = hashtag.post_set.order_by('-pk')
    context = {
        'hashtag': hashtag,
        'posts': posts,
    }
    return render(request, "posts/hashtag.html", context)
