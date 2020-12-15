from rest_framework import routers

from blog import views


router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

