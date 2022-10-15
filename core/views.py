from re import template
from unicodedata import category
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from core.forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from product.models import ProductModel


# Home view
class HomeView(views.TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = ProductModel.objects.filter(status=True)
        context["products"] = products
        return context


# About view
class AboutView(views.TemplateView):
    template_name = "core/about.html"


# add to cart view
class AddToCartView(views.View):
    def post(self, request):
        pass


# remove from cart view
class RemoveFromCartView(views.View):
    def post(self, request, pk):
        pass


# cart view
class CartDetailView(views.DetailView):
    template_name = "core/cart_detail.html"


# checkout view
class CheckoutView(views.View):
    template_name = "core/checkout.html"

    def get(self, request):
        pass

    def post(self, request):
        pass


# Payment view
class PaymentView(views.View):
    template_name = "core/payment.html"

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


# Payment view
class OrderHistoryView(views.ListView):
    template_name = "core/order_history.html"


# Payment view
class OrderDetailView(views.DetailView):
    template_name = "core/order_detail.html"



#login view
class LoginView(views.View):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("core:home")

    def get(self,request):
        context = {
            "form": self.form_class()
        }
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data("username")
            password = data("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(self.success_url)
        return render(request,self.template_name,{"form":form})


#user register view
class UserRegisterView(views.View):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def get(self,request):
        context = {
            "form":self.form_class()
        }
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            print("Form valid")
            return redirect(self.success_url)
        print("Form INvalid")
        return render(request,self.template_name,{"form":form})

#product by category view
class ProductByCategoryView(views.ListView):
    template_name = "core/home.html"
    model = ProductModel
    context_object_name = "products"

    def get_queryset(self):
        qs = super() . get_queryset()
        qs = qs.filter(category__name__iexact = self.kwargs.get("category",None))

        return qs



#contact view
class ContactView(views.View):
    template_name = "core/contact.html"
    form_class = ContactForm
    

    def get(self, request):
        context = {
            "form": self.form_class(),
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
    def form_valid(self, form):
        data = form.cleaned_data
        name = data.get("name")
        subject = "Thanks for your valuable feedback"
        to_email = data.get("email")
        message = data.get("message")
        from_email = settings.EMAIL_HOST_USER
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=[
                    to_email,
                ],
            )
            form.save()
            messages.success(self.request, "Thanks for your valuable feedback!")

        except:
            messages.error(self.request, "Can not send feedback! Please try again!")
        return redirect(reverse_lazy("core:contact"))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {"form": form})

    
        








