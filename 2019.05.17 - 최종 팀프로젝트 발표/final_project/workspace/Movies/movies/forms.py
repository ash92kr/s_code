from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Movie, Comment, Actor, Genre

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['score', 'content',]
        widgets = {'score': forms.NumberInput(attrs={
                                                'placeholder': '평점을 선택하세요',
                                                'class': 'score',
                                                'max_value': 10,
                                                'min_value': 0,}),
                  'content': forms.TextInput(attrs={
                                                'placeholder': '내용을 입력하세요',
                                                'class': 'content',}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()   # 폼 헬퍼
        self.helper.form_method = 'POST'  # 메소드
        self.helper.add_input(Submit('submit', '작성'))   # 버튼
        
        
        