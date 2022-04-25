from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Feed(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='gallery')