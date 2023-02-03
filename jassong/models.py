from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)


class Audio(models.Model):
    title = models.CharField(max_length=100)
    audio_src = models.FileField(upload_to='jassong/Audios/')


# class Videos(models.Model):
#     title = models.CharField(max_length=255)
#     video_src = models.FileField(upload_to='jassong/Videos/')
#
#
# class Images(models.Model):
#     title = models.CharField(max_length=255)
#     upload = models.FileField(upload_to='jassong/Images/')
#

