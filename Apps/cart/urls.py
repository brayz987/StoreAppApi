from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'detail', CartView, basename="cart")
router.register(r'history', HistoryView, basename="history")

urlpatterns = [
    path('', include(router.urls)),
    path('generateJson/', GenerateHistoryView.as_view())
]