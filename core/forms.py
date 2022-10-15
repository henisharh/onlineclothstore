from dataclasses import fields
from pyexpat import model
from django import forms
from django import forms
from core import views

from core.models import CartModel, ContactModel, OrderModel, PaymentModel


class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = []


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = []


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = []



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ("is_replied", "status", "user")
