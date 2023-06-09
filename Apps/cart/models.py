from django.db import models
from Apps.user.models import CustomUserModel
from Apps.product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(CustomUserModel,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'Usuario {self.user.last_name} {self.user.first_name} - Producto {self.product.name}'

class History(models.Model):
    user = models.ForeignKey(CustomUserModel,  on_delete=models.CASCADE)
    config = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'Usuario {self.user.last_name} {self.user.first_name} - Fecha {self.created_at}'