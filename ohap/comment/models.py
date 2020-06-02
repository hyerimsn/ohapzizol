from django.db import models
from django.utils import timezone
# Create your models here.

class Temp(models.Model):
    title = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Temp, on_delete=models.CASCADE)
    body = models.CharField('댓글',max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.CharField('대댓글',max_length=150)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body