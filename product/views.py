from itertools import product
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from product import forms, models

# Create view
#class ProductCreateView(views.CreateView):
 #   template_name = "product/create.html"
  #  model = models.ProductModel
   # form_class = forms.ProductForm
    #success_url = reverse_lazy("product:product_list")

# list view
#class ProductListView(views.ListView):
 #   template_name = "product/list.html"
  #  model = models.ProductModel
   # context_object_name = "products"

# Detail view
class ProductDetailView(views.DetailView):
    template_name = "product/detail.html"
    model = models.ProductModel
    context_object_name = "product"

# Update view
# class ProductUpdateView(views.UpdateView):
#     template_name = "product/update.html"
#     model = models.ProductModel
#     form_class = forms.ProductForm
#     success_url = reverse_lazy("product:product_list")

# Delete View
# class ProductDeleteView(views.DeleteView):
#     template_name = "product/delete.html"
#     model = models.ProductModel
#     success_url = reverse_lazy("product:product_list")

#ProductCategoryModel

#create view
class ProductCategoryCreateView(views.CreateView):
    template_name = "product/category/create.html"
    model = models.ProductCategoryModel
    success_url = reverse_lazy("productcategory:productcategory_list")

#list view
class ProductCategoryListView(views.ListView):
    template_name = "product/category/list.html"
    model = models.ProductCategoryModel
    context_object_name = "categories"

#detail view
class ProductCategoryDetailView(views.DetailView):
    template_name = "product/category/detail.html"
    model = models.ProductCategoryModel
    context_object_name = "category"

#update view
class ProductCategoryUpdateView(views.UpdateView):
    template_name = "product/category/update.html"
    model = models.ProductCategoryModel
    form_class = forms.ProductCategoryForm
    success_url = reverse_lazy("productcategory:productcategory_list")

#delete view
class ProductCategoryDeleteView(views.DeleteView):
     template_name = "product/category/delete.html"
     model = models.ProductCategoryModel
     success_url = reverse_lazy("productcategory:productcategory_list")


#simple view

#list view
class ProductListView(views.View):
    template_name ="product/list.html"
    model = models.ProductModel

    def get(self,request):
        products = self.model.objects.all()
        context = {
            "products" : products
            }
        return render(request, self.template_name, context)
        
#create view
class ProductCreateView(views.View):
    template_name = "product/create.html"
    model = models.ProductModel
    success_url = reverse_lazy("product:product_list")
    form_class = forms.ProductForm

    def get(self,request):

        context = {
            "form":self.form_class()
        }
        return render(request,self.template_name,context)

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(self.success_url)
        else:
            return render(request,self.template_name,{"form":form})

#update view
class ProductUpdateView(views.View):
    template_name = "product/Update.html"
    model = models.ProductModel
    success_url = reverse_lazy("product:product_list")
    form_class = forms.ProductForm

    def get(self,request,pk):
        product = models.ProductModel.objects.get(id=pk)
        context = {
            "form":self.form_class(instance=product)
        }
        return render(request,self.template_name,context)

    def post(self,request, pk):
        product = models.ProductModel.objects.get(id=pk)
       
        form = self.form_class(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(self.success_url)
        else:
            return render(request,self.template_name,{"form":form})


#delete view
class ProductDeleteView(views.DeleteView):
    template_name = "product/delete.html"
    model = models.ProductModel
    success_url = reverse_lazy("product:product_list")

    def get(self,request,pk):
        context ={

        }
        return render(request, self.template_name)

    def post(self, request,pk):
        product = models.ProductModel.objects.get(id=pk)
        product.delete()
        return redirect(self.success_url)
