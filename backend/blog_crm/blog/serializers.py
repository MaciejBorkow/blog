from rest_framework import serializers

from blog.models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'author', 'image']
