import uuid

from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import parsers
from faker import Faker

from blog.models import Article
from blog.serializers import ArticlesSerializer

fake = Faker()


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer


class ArticlePostView(views.APIView):
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser]
    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticlesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return Response({'yes': 'yes'})


@csrf_exempt
def file_view(request):
    file_name = str(uuid.uuid4()) + '.jpg'
    file = SimpleUploadedFile(name=file_name, content=request.body, content_type='image/png')
    a = Article.objects.create(
        title=fake.text(max_nb_chars=12),
        body=fake.paragraph(nb_sentences=15),
        image=file,
    )
    return JsonResponse({'id': a.id})
