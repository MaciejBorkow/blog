from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    background_uri = models.CharField(blank=True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
