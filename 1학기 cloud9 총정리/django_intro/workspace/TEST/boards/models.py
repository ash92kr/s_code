from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length = 30)
    # content = models.Charfield(max_length = 100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # 자동으로 생성, 수정될 때 더해지는 부분 - views.py에는 넣지 않음
