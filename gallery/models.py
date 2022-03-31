from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.post.title