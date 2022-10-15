from unicodedata import name
from django.conf import settings
from django.db import models


USER = settings.AUTH_USER_MODEL


class ProductUnitModel(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}({self.symbol})"


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name}({self.symbol})"


class ProductBrandModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to="product/category/image/", default="default/category.jpg"
    )
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(upload_to="product/image/", default="default/product.jpg")
    category = models.ForeignKey(
        "ProductCategoryModel", on_delete=models.SET_NULL, null=True
    )
    unit = models.ForeignKey("ProductUnitModel", on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey("ProductSizeModel", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey("ProductBrandModel", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
