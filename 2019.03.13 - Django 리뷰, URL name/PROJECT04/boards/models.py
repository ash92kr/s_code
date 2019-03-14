from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # 갱신될 때마다 시간이 바뀜
    
    def __str__(self):   # 이 부분도 자동으로 입력하기
        return f"{self.id}: {self.title}"
        # return self.title