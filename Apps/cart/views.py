
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
import logging

# Create your views here.
class CartView(ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user, is_active=True)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CartCreateSerializer
        request.data['user'] = self.request.user.id
        return super().create(request, *args, **kwargs)


class HistoryView(ModelViewSet):
    serializer_class = HistorySerializer

    def get_queryset(self):
        user = self.request.user
        return History.objects.filter(user=user, is_active=True)


class GenerateHistoryView(APIView):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        cartObj = Cart.objects.filter(
            user=user, is_active=True).values("product", "amount")
        cartJson = [entry for entry in cartObj]

        if len(cartJson) > 0:

            try:
                history = History()
                history.config = cartJson
                history.user = self.request.user
                history.save()
            except Exception as error:
                return Response({"state": "error", "message": "Error al crear el historial", "system_error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            try:
                cartObj.update(is_active=False)
            except Exception as error:
                return Response({"state": "error", "message": "Error al limpiar el carrito", "system_error": error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            return Response({"state": "success", "message": "Historico Guardado", "system_error": None})
        else:
            return Response({"state": "success", "message": "Sin compras", "system_error": None})


