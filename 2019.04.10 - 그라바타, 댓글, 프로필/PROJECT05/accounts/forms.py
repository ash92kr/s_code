from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserCustomChangeForm(UserChangeForm):  # 이런식으로 Custom을 중간에 넣음
    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name',]  # 이 필드들을 가져옴 - https://docs.djangoproject.com/en/2.2/ref/contrib/auth/
        fields = ['email', 'first_name', 'last_name',]   # username은 변경 불가

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email',]
        # 회원 가입시 4개 필드의 내용을 입력해야 한다
        