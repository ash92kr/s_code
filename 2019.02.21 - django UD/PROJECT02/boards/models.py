from django.db import models

# Create your models here.
class Board(models.Model):   # 모델 만들기 - 각 모델은 django.db.models.Model 클래스의 서브 클래스로 표현됨
    title = models.CharField(max_length=10)   # title 필드는 최대 10글자 들어감(max_length는 charfield의 필수인자)
    content = models.TextField()   # 내용에 제한이 없음
    created_at = models.DateTimeField(auto_now_add=True)   # 글을 작성한 시간이 기록됨 - UTC 기준
    # settings.py의 USE_TZ를 False로 바꿔야 seoul 시간이 사용됨
    # auto_now_add는 장고 모델이 최초 저장시에만 현재 날짜를 적용한다
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now는 장고 모델이 save 될때마다 현재 날짜로 갱신됨

    def __str__(self):
        return f'{self.id}: {self.title}'   # 출력되는 방식을 바꿈


