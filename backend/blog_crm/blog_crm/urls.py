from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.urls import router
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('file', views.file_view, name='dupa'),
    path('article_test', views.ArticlePostView.as_view()),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
