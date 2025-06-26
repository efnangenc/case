from django.db import models
from .album import Album

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255)
    url = models.URLField()
    thumbnailUrl = models.URLField()

    def __str__(self):
        return self.title
