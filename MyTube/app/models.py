from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User



class Comment(models.Model):
    video = models.ForeignKey('studio.Video', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, related_name='comment_dislikes')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


    def count_replies(self):
        return Comment.objects.filter(parent=self).count()



