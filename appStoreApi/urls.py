
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView





urlpatterns = [
    path('secret/', admin.site.urls),
    path('', include('Apps.api.urls') ),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
