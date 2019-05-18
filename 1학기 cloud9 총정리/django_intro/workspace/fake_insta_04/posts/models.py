from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content
    
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    content = models.TextField()

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

# user.post_set
# post.user

# post.user 
# post.like_users

# user.post_set 유저가 작성한 글들
# user.like_posts 유저가 좋아요 누른 글들
# user.post_set
# 유저가 좋아요한 post? user.like_posts
# post 에 좋아요한 유저들 post.like_posts
