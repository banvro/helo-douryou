from unicodedata import category
from django.db import models

# Create your models here.


class AddnewVideo(models.Model):
    video_name=models.CharField(max_length=255)
    category_name=models.CharField(max_length=255)
    video_title=models.CharField(max_length=255)
    select_seller=models.CharField(max_length=255)
    video_link=models.CharField(max_length=255)
    thumbnail_link=models.CharField(max_length=255)


    def __str__(self):
        return self.video_name