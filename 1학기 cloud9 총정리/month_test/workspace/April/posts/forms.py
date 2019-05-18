from django import forms
from .models import Post

# Q2-1 문제의 답안 코드를 아래에 작성하세요.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]
        