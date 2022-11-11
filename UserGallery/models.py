from django.db import models
from  django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    demo = models.CharField(max_length=100)

    def __str__(self):
        return self.email



class PlayList(models.Model):
    title = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)


class Video(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField()
    youtube_id = models.CharField(max_length=100)
    playlist = models.ForeignKey(PlayList,on_delete=models.CASCADE)
