from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    title = models.CharField(max_length=50, blank=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    background = models.ImageField(upload_to='article_images', null=True)
    published = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=20)
    articles = models.ManyToManyField(Article, related_name='tags')


class Keyword(models.Model):
    name = models.CharField(max_length=123)


class Policy(models.Model):
    keywords = ArrayField(models.CharField(max_length=12), default=list)
