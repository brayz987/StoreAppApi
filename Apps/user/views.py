

from django.http import Http404
from .models import CustomUserModel
from .serializers import UserSerializer,UpdateUserSerializer,PasswordUpdateSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.test import APIClient


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class InformationUserView(APIView):

    def get_object(self, pk):
        try:
            return CustomUserModel.objects.get(pk=pk)
        except CustomUserModel.DoesNotExist:
            raise Http404
        

    def get(self, request, format=None):
        userObj = request.user
        data = UserSerializer(userObj).data
        return Response(data)
    
    def put(self, request, format=None):
        user = request.user
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        user = request.user
        user.is_active = False
        user.save()
        return Response({"message": "The user has been deleted"})
        


class PasswordUserView(APIView):

    def put(self, request, format=None):
        user = request.user
        serializer = PasswordUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The password has been successfully updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    