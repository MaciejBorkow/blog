from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    data = models.ImageField(upload_to='article_images')


class Tag(models.Model):
    name = models.CharField(max_length=20)
    articles = models.ManyToManyField(Article)
