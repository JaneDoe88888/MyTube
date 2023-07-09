from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(upload_to='video/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    created_add = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    views = models.IntegerField(default=0)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

