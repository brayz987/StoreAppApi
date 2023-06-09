
from django.http import Http404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .models import *
from .serializers import *

# Create your views here.
class ProductView(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    parser_classes = [FormParser, MultiPartParser,JSONParser]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryView(ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ProductImageView(ModelViewSet):
    serializer_class = ProductImageSerializer
    parser_classes = [FormParser, MultiPartParser,JSONParser]

    def get_queryset(self):
        queryset = ProductImage.objects.filter(is_active=True)
        product = self.request.query_params.get('product')
        if product is not None:
            queryset = queryset.filter(product=product)
        return queryset


class DiscountProductView(ModelViewSet):
    queryset = DiscountProduct.objects.filter(is_active=True)
    serializer_class = DiscountProductSerializer
