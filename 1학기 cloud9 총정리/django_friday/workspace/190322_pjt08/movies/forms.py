from django import forms
from .models import Genre, Movie, Score

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                                        'placeholder': '영화 제목 입력',
                                        'class': 'title',}),
            'audience': forms.NumberInput(attrs={
                                        'placeholder': '관객수 입력',
                                        'class': 'audience',}),
            'poster_url': forms.Textarea(attrs={
                                        'placeholder': '포스터 url 입력',
                                        'class': 'poster_url',
                                        'rows': 2,
                                        'cols': 100,}),
            'description': forms.Textarea(attrs={
                                        'placeholder': '영화 설명 입력',
                                        'class': 'description',
                                        'rows': 5,
                                        'cols': 100,}),
            'genre': forms.NumberInput(attrs={
                                        'placeholder': '장르 번호 입력',
                                        'class': 'genre',
                                        'max_value': 11,
                                        'min_value': 1,}),
                    }
                    
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'
        widgets = {
            'content': forms.TextInput(attrs={
                                        'placeholder': '감상평 입력',
                                        'class': 'content',}),
            'score': forms.NumberInput(attrs={
                                        'placeholder': '평점 입력',
                                        'class': 'score',
                                        'max_value': 5,
                                        'min_value': 0,}),
        }