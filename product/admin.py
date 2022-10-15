import imp
from django.contrib import admin
from product import models


admin.site.register(models.ProductModel)
admin.site.register(models.ProductCategoryModel)
admin.site.register(models.ProductUnitModel)
admin.site.register(models.ProductSizeModel)
admin.site.register(models.ProductBrandModel)