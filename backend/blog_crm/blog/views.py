from django.shortcuts import render
from rest_framework import viewsets

from blog.models import Article
from blog.serializers import ArticlesSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
