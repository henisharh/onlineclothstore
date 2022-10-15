from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("" , views.HomeView.as_view(),name="home"),
    path("about/" , views.AboutView.as_view(),name="about"),
    path("add_to_cart/" , views.AddToCartView.as_view(),name="add_to_cart"),
    path("remove_from_cart/" , views.RemoveFromCartView.as_view(),name="remove_from_cart"),
    path("cart_detail/" , views.CartDetailView.as_view(),name="cart_detail"),
    path("checkout/" , views.CheckoutView.as_view(),name="checkout"),
    path("payment/" , views.PaymentView.as_view(),name="payment"),
    path("order_detail/<int:pk>/" , views.OrderDetailView.as_view(),name="order_detail"),
    path("order_history/" , views.OrderHistoryView.as_view(),name="order_history"),
    path("user_registration/" , views.UserRegisterView.as_view(),name="user_registration"),
    path("product_by_category/<str:category>/",views.ProductByCategoryView.as_view(),name="product_by_category"),
    path("contact/" , views.ContactView.as_view(),name="contact"),

]

