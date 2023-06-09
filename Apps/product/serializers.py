from .models import *
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image","product"]

class ProductImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]
    
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageUrlSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True, required=False
    )

    class Meta:
        model = Product
        fields = "__all__"
    
    def get_fields(self):
        fields = super().get_fields()
        fields.pop("is_active")
        return fields
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = super().create(validated_data)

        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product


        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        fields.pop("is_active")
        return fields


class DiscountProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountProduct
        fields = "__all__"
    def get_fields(self):
        fields = super().get_fields()
        fields.pop("is_active")
        return fields