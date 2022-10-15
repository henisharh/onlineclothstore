import email
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()

class CartModel(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)


class CartItemModel(models.Model):
    cart = models.ForeignKey("core.CartModel", on_delete=models.CASCADE)
    product = models.ForeignKey("product.ProductModel", on_delete=models.CASCADE)
    quanitity = models.PositiveIntegerField()


class OrderModel(models.Model):
    cart = models.ForeignKey("core.CartModel", on_delete=models.CASCADE)
    billing_address = ""
    shipping_address = ""
    is_completed = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)



class PaymentModel(models.Model):
    order = models.ForeignKey("core.OrderModel", on_delete=models.CASCADE)
    status = models.CharField(max_length=24)


class ContactModel(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)





