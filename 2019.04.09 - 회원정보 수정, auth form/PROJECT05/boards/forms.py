from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Board

# class BoardForm(forms.Form):
#     title = forms.CharField(label='제목', widget=forms.TextInput(attrs={
#                                                         'placeholder': 'THE TITLE',   # 기본값 입력
#                                             }))
#     content = forms.CharField(label='내용',
#                               error_messages={'required': '내용을 입력하세요!'},
#                               widget=forms.Textarea(attrs={
#                                                     'class': 'Content-input',   # 클래스
#                                                     'rows': 5,   # 행 수
#                                                     'cols': 50,  # 열 수
#                                                     'placeholder': 'Fill the Content',
#                                             }))

class BoardForm(forms.ModelForm):
    class Meta:  # 클래스 설명(Model의 정보를 작성하는 곳)
        model = Board
        fields = ['title', 'content',]   # 필드가 많으면 아래와 같이 작성
        # fields = '__all__'  # models.py에 지정한 필드를 사용한다
        widgets = {'title': forms.TextInput(attrs={
                                                'placeholder': '제목을 입력하세요',
                                                'class': 'title',}),
                  'content': forms.Textarea(attrs={
                                                'placeholder': '내용을 입력하세요',
                                                'class': 'content',
                                                'rows': 5,
                                                'cols': 50,})
                    }
        error_messages = {'title': {
                                    'required': '제발 입력해주세요!'
                                    },
                          'content': {
                                    'required': '내용 입력하세요!'
                          },
                        }               
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()   # 폼 헬퍼
        self.helper.form_method = 'POST'  # 메소드
        self.helper.add_input(Submit('submit', '작성'))   # 버튼
    