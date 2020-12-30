from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include

from blog import views


router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'tag', views.TagViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('article/<int:article_id>/tag/<int:tag_id>/', views.ArticleAddDeleteTagsView.as_view()),
]
a = 1
