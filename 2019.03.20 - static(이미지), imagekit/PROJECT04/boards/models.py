from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def board_image_path(instance, filename):
    return f'boards/{instance.pk}/images/{filename}'
    # return f'boards/{instance.user.username}/images/{filename}'

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
                # upload_to = 'boards/images',   # 업로드 된 파일은 media에 들어가므로 media에 boards 폴더가 만들어진다(저장 위치)
                upload_to = board_image_path,
                processors = [ResizeToFill(200, 300)],   # 처리할 작업 목록
                format = 'JPEG',  # 포멧을 변환해서 업로드한다(저장 포맷)
                options = {'quality': 90},   # 옵션
        )
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