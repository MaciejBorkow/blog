from django.contrib.auth.models import User
from rest_framework import serializers

from blog import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ['id', 'name']


class ArticlesSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Tag.objects.all())

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'body', 'background', 'author', 'published', 'tags']
