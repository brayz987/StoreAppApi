
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('secret/', admin.site.urls),
    # path('user/', include('Apps.user.urls') ),
    # path('product/', include('Apps.product.urls') ),
    # path('cart/', include('Apps.cart.urls') ),


    path('api/', include('Apps.api.urls') ),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
