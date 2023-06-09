
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.
class CartView(ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user,is_active=True)

class HistoryView(ModelViewSet):
    serializer_class = HistorySerializer
    def get_queryset(self):
        user = self.request.user
        return History.objects.filter(user=user,is_active=True)