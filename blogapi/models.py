from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    audio_path = models.CharField(max_length=255)
    file_size = models.FloatField()
    view  = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.blog_id