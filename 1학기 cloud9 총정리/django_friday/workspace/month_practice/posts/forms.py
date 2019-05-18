from django import forms
from .models import Post

class PostForm(forms.ModelForm):   # 이게 모델폼이다
    class Meta:
        model = Post
        fields = ['title', 'content',]
        widgets = {'title': forms.TextInput(attrs={
                                            'placeholder': '제목을 입력해주세요',
                                            'class': 'title'}),
                    'content': forms.Textarea(attrs={
                                            'placeholder': 'content-input',
                                            'rows': 5,
                                            'cols': 50,
                                            'placeholder': '거기 누구 있소?',})}
        error_messages = {'title': {
                                    'required': '제목을 반드시 입력해주세요.'
                                    },
                          'content': {
                                    'required': '내용을 반드시 입력하라.'
                                     },
                         }


