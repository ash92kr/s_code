from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'updated_at',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
