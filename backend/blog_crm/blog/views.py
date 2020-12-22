from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from blog.models import Article, Tag
from blog.serializers import ArticlesSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=['delete'], detail=True)
    def background(self, request, pk=None):
        article = self.get_object()
        if article.background:
            article.background.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True)
    def tags(self, requset, pk=None):
        article = self.get_object()
        serializer = TagSerializer(instance=article.tags, many=True)
        return Response(serializer.data)


class ArticleTagsView(generics.GenericAPIView):
    queryset = Article.objects.all()
    lookup_url_kwarg = 'article_id'

    def put(self, request, *args, **kwargs):
        article = self.get_object()
        article.tags.add(kwargs['tag_id'])
        return Response(status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        article.tags.remove(kwargs['tag_id'])
        return Response(status.HTTP_200_OK)
