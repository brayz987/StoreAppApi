from .models import *
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id","product","amount","created_at"]

class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id","product","amount","created_at","user"]

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["id", "config", "created_at"]