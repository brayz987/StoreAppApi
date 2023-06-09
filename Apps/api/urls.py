
from django.urls import path, include, re_path

urlpatterns = [
    path('user/', include('Apps.user.urls') ),
    path('product/', include('Apps.product.urls') ),
    path('cart/', include('Apps.cart.urls') ),
]