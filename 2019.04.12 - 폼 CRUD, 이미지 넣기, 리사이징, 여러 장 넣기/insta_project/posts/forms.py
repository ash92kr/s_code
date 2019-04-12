from django import forms
from .models import Post, Image   # Post 모델을 가져옴

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True}),
        }   # 중복 이미지 선택 가능