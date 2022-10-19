from pyexpat import model
from django import forms

from product.models import ProductCategoryModel #, ProductModel


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = ProductModel
#         exclude = ["user", "status", "created_on", "updated_on"]

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryModel
        exclude = ["user", "status", "created_on", "updated_on"]