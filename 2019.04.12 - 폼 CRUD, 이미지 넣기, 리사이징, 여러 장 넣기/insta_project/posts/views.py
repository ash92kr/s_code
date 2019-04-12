from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Post
from .forms import PostForm, ImageForm

# Create your views here.
def list(request):
    posts = get_list_or_404(Post.objects.order_by('-pk'))
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)


def create(request):
    if request.method == "POST":
        # post_form = PostForm(request.POST, request.FILES)   # POST를 통해 받아들인 것
        post_form = PostForm(request.POST)
        if post_form.is_valid():           # 이미지는 FILES에 들어간다
            post = post_form.save()   # 게시글 처리 끝
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


def update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)   # 수정을 위한 입력된 값, instance 순서로 받아옴
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)   # 기존에 입력한 값을 instance로 받아온다
    context = {
        'post_form': post_form,
    }
    return render(request, 'posts/form.html', context)
    
    
def delete(request, post_pk):   # post_pk는 변수명으로 사용되는 것으로, 아무 이름이나 사용해도 된다
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        post.delete()
    return redirect('posts:list')