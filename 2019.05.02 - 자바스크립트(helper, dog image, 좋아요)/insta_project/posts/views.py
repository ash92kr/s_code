from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q
from itertools import chain
from django.http import JsonResponse
from .models import Post, Image, Comment, Hashtag
from .forms import PostForm, ImageForm, CommentForm


# Create your views here.
@login_required
def list(request):
    # posts = get_list_or_404(Post.objects.order_by('-pk'))
    # posts = Post.objects.filter(user__in=request.user.followings.all()).order_by('-pk')
    
    # 1. Q object 사용
    followings = request.user.followings.all()   # 내가 follow하는 user 리스트
    posts = Post.objects.filter(Q(user__in=followings) | Q(user=request.user.id)).order_by('-pk')
    
    # 2. chain 사용
    # followings = request.user.followings.all()  # 내가 follow하는 user 리스트
    # chain_followings = chain(followings, [request.user])  # followings 변수(쿠리셋)와 나(리스트)를 묶음
    # posts = Post.objects.filter(user__in=chain_followings).order_by('-pk')   # 이들이 작성한 post만 뽑음
    
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/list.html', context)



@login_required
def create(request):
    if request.method == "POST":
        # post_form = PostForm(request.POST, request.FILES)   # POST를 통해 받아들인 것
        post_form = PostForm(request.POST)
        if post_form.is_valid():           # 이미지는 FILES에 들어간다
            post = post_form.save(commit=False)   # 게시글 처리 끝
            post.user = request.user
            post.save()
            # hashtag = post.content에 hashtag를 사용하므로 저장된 이후에 넣어야 한다
            # 1. 게시글을 순회하면서 띄어쓰기로 구분해야함
            # contents = post.content.split()
            for word in post.content.split():
            # 2. 자른 단어는 #으로 시작하는가?
            # for content in contents:
                # if word[0] == "#":
                if word.startswith('#'):
                    hashtag = Hashtag.objects.get_or_create(content=word)   # .get or .create -> hashtag의 인스턴스나 boolean을 return(기존에 없으면 True, 기존에 있으면 False)
            # 3. 이 해시태그가 기존 해시태그에 있는 것인가?
                    # if content not in Hashtag.objects.all():
                        # hashtag = Hashtag()
                        # hashtag.content = content[1:]
                        # hashtag.save()
                    # if new:
                        # post.hashtags.add(hashtag)   # hashtag의 모든 집단에 hashtag를 넣음
                    post.hashtags.add(hashtag[0])  # 2가지가 tuple로 반환되므로 첫번째만 넣음(hashtag, True or False) -> False면 get을 하고, True면 create을 한다

            # 이미지 여러 장 받기
            for image in request.FILES.getlist('file'):  # file의 이미지들을 하나씩 돌면서 검증
                request.FILES['file'] = image  # file에 image를 넣어준다
                image_form = ImageForm(files=request.FILES)  # 이미지 폼을 불러온다
                if image_form.is_valid():
                    image = image_form.save(commit=False)   # 아직 이미지 저장하지 말고
                    image.post = post   # 어떤 게시글인지 알려주어야 한다
                    image.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()   # 중복방지용 이름
        image_form = ImageForm()
    context = {
        'post_form': post_form,
        'image_form': image_form,
    }
    return render(request, 'posts/form.html', context)

@login_required
def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)   # 수정을 위한 입력된 값, instance 순서로 받아옴
        if post_form.is_valid():
            post_form.save()
            # hashtag update
            post.hashtags.clear()   # 모든 해시태그 삭제함
            for word in post.content.split():   # 수정한 글로부터 다시 해시태그 만들기
                if word.startswith("#"):
                    hashtag = Hashtag.objects.get_or_create(content=word)
                    post.hashtags.add(hashtag[0])
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)   # 기존에 입력한 값을 instance로 받아온다
    context = {
        'post_form': post_form,
    }
    return render(request, 'posts/form.html', context)
    
    
def delete(request, post_pk):   # post_pk는 변수명으로 사용되는 것으로, 아무 이름이나 사용해도 된다
    post = get_object_or_404(Post, pk=post_pk)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == "POST":
        post.delete()
    return redirect('posts:list')
    
    
@login_required
@require_POST
def comment_create(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_pk
        comment.save()
    return redirect('posts:list')
    

@login_required
@require_POST
def comment_delete(request, post_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:   # 본인이 작성한 댓글만 삭제되도록 함
        return redirect('posts:list')
    comment.delete()
    return redirect('posts:list')


@login_required
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user in post.like_users.all():  # 좋아요를 누른 모든 user에 있으면
        post.like_users.remove(request.user)   # 좋아요 제거
        liked = False
    else:                                      # 없으면 
        post.like_users.add(request.user)      # 좋아요에 추가
        liked = True
    # return redirect('posts:list')
    context = {
        'liked': liked,
        'count': post.like_users.count(),   # 좋아요 수를 넘겨줌
    }
    return JsonResponse(context)
    

@login_required
def explore(request):
    posts = Post.objects.order_by('-pk')
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        }
    return render(request, 'posts/explore.html', context)


def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    posts = hashtag.post_set.order_by('-pk')   # 역참조(게시글이 해시태그를 참조함)
    context = {
        'hashtag': hashtag,
        'posts': posts,
    }    
    return render(request, 'posts/hashtag.html', context)
    