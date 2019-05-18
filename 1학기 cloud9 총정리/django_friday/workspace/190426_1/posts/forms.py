from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="")   # label 삭제
    class Meta:
        model = Comment
        fields = ['content',]