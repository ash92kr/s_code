from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):    # Meta class 도 상속받을 수 있다.
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','introduction','favorite_genre']
        
        FAVORITE_GENRE_CHOICE = (
            ('가족','가족'),('공포(호러)','공포(호러)'),('다큐멘터리','다큐멘터리'),('드라마','드라마'),
            ('멜로/로맨스','멜로/로맨스'),('뮤지컬','뮤지컬'),('미스터리','미스터리'),('범죄','범죄'),
            ('사극','사극'),('서부극(웨스턴)','서부극(웨스턴)'),('스릴러','스릴러'),('애니메이션','애니메이션'),('액션','액션'),
            ('어드벤처','어드벤처'),('전쟁','전쟁'),('코미디','코미디'),('판타지','판타지'),('SF','SF')
            )
            
        widgets = {
            'introduction': forms.Textarea,
            'favorite_genre': forms.Select(choices=FAVORITE_GENRE_CHOICE),
        }
    
