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
        

class Comment(models.Model):   # 외래키 속성은 어디에 두든지 간에 가장 마지막 속성에 붙는다
    board = models.ForeignKey(Board, on_delete=models.CASCADE)   # Board 테이블 참조하며, 
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content