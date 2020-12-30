from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, filters

from blog.models import Article, Tag
from blog.serializers import ArticlesSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()  # filter(published=False) TODO
    serializer_class = ArticlesSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'body']
    ordering_fields = ['created', 'updated']
    ordering = ['-updated']

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
    def tags(self, request, pk=None):
        article = self.get_object()
        serializer = TagSerializer(instance=article.tags, many=True)
        return Response(serializer.data)


class ArticleAddDeleteTagsView(generics.GenericAPIView):
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
