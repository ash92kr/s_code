from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)




