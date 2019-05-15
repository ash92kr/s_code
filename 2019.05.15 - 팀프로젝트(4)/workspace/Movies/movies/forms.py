from django import forms
from .models import Movie, Comment, Actor, Genre

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['score', 'content',]
        # widgets = {'score': forms.NumberInput(attrs={
        #                                         'placeholder': '평점을 선택하세요',
        #                                         'class': 'score',}),
        #           'content': forms.TextInput(attrs={
        #                                         'placeholder': '내용을 입력하세요',
        #                                         'class': 'content',})
        # }