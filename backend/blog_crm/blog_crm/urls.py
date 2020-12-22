from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.urls import urlpatterns as blog_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include((blog_urlpatterns, 'blog')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
