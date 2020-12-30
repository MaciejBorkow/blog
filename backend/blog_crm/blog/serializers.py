from django.contrib.auth.models import User
from rest_framework import serializers

from blog import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['id', 'url', 'name']


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = models.Article
        fields = [
            'id', 'url', 'title', 'body', 'background',
            'author', 'published', 'tags', 'created', 'updated',
        ]
