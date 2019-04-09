from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserCustomChangeForm(UserChangeForm):  # 이런식으로 Custom을 중간에 넣음
    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name',]  # 이 필드들을 가져옴 - https://docs.djangoproject.com/en/2.2/ref/contrib/auth/
        fields = ['email', 'first_name', 'last_name',]   # username은 변경 불가
