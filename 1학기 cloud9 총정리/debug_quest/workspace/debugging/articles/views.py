from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})
    
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    return render(request, 'articles/create.html', {'article_form': article_form})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comment_form = CommentForm()
    return render(request, 'articles/detail.html', {'article': article, 'comment_form': comment_form})

@login_required
def update(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user != request.user:
        return HttpResponseForbidden("You are not allowed to update this Article")
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    return render(request, 'articles/update.html', {'article_form': article_form})

@login_required
def delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this Article")
    article.delete()
    return redirect('articles:list')
    
@require_POST
@login_required
def comment_create(request, article_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article_id)

@require_POST
@login_required
def comment_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this Comment")
    comment.delete()
    return redirect('articles:detail', article_id)