from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=500, null=False)
    description = models.TextField()
    price = models.IntegerField(null=False, default=0)
    category = models.ManyToManyField(Category, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='productsImages/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.product.name


class DiscountProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    percentage = models.IntegerField()
    valid = models.DateField()
    activate = models.BooleanField()
    inStock = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product.name
    



