from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'detail', ProductView, basename="product")
router.register(r'category', CategoryView, basename="category")
router.register(r'images', ProductImageView, basename="images")
router.register(r'discount', DiscountProductView, basename="discount")

urlpatterns = [
    path('', include(router.urls))
]