from django.urls import path, include
from product import views


app_name = "product"

urlpatterns = [
    path("create/", views.ProductCreateView.as_view(), name="product_create"),
    path("list/", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/detail/", views.ProductDetailView.as_view(), name="product_detail"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),

    path("category/create/", views.ProductCategoryCreateView.as_view(), name="productcategory_create"),
    path("category/list/", views.ProductCategoryListView.as_view(), name="productcategory_list"),
    path("category/<int:pk>/detail/", views.ProductCategoryDetailView.as_view(), name="productcategory_detail"),
    path("category/<int:pk>/update/", views.ProductCategoryUpdateView.as_view(), name="productcategory_update"),
    path("category/<int:pk>/delete/", views.ProductCategoryDeleteView.as_view(), name="productcategory_delete"),
    

    




]

