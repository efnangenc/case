from django.db import models
from .user import User

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
