from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def question_image_path(instance, filename):
    return f'votes/{instance.pk}/images/{filename}'

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    select_a = models.TextField()
    select_b = models.TextField()
    # image_a = models.ImageField(blank=True)
    # image_b = models.ImageField(blank=True)
    image_a = ProcessedImageField(
                upload_to = question_image_path,
                processors = [ResizeToFill(200,300)],
                format = 'JPEG',
                options = {'quality': 90},
    )
    image_b = ProcessedImageField(
                upload_to = question_image_path,
                processors = [ResizeToFill(200,300)],
                format = 'JPEG',
                options = {'quality': 90},
    )
    
    def __str__(self):
        return f"{self.title}, {self.select_a}, {self.select_b}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()
    
    def __str__(self):
        return f'{self.pick}, {self.comment}'