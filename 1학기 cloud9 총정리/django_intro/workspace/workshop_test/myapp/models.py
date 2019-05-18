from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()