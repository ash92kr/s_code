from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Hashtag(models.Model):   # hashtag가 먼저 선언되어야 아래에서 적을 수 있다
    content = models.TextField(unique=True)   # 같은 hashtag는 하나로 모아져야 한다
    
    def __str__(self):
        return self.content
        

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)   # 특정 게시글에는 hashtag가 없어도 된다 -> 역참조 에러가 발생하지 않아 related_name을 넣지 않음
    content = models.TextField()
    # image = models.ImageField(blank=True)   # 빈 값도 들어갈 수 있게
    # image = ProcessedImageField(
    #             upload_to='posts/images',
    #             processors=[ResizeToFill(600, 600)],
    #             format='JPEG',
    #             options={'quality': 90},
    #         )
    
    def __str__(self):
        return self.content


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
                upload_to='posts/images',
                processors=[ResizeToFill(600, 600)],
                format='JPEG',
                options={'quality': 90},
            )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return self.content