
# Create your models here.
from django.db import models

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    picUrl = models.CharField(max_length=255)
    content = models.TextField()
    audio_path = models.CharField(max_length=255)
    file_size = models.FloatField()
    view  = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)


class dashb(models.Model):
      dash_d_id = models.AutoField(primary_key=True)
      view_d = models.IntegerField()
      date_d = models.DateField()


def __str__(self):
        return self.blog_id


def __str__(self):
        return self.dash_d_id



