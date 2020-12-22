from rest_framework import routers
from django.urls import path

from blog import views


router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
    path('article/<int:article_id>/tag/<int:tag_id>/', views.ArticleTagsView.as_view()),
]

urlpatterns += router.urls
