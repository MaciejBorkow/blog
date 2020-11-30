from rest_framework import routers

from blog.views import ArticleViewSet


router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
