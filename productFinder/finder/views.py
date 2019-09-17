from django.shortcuts import render,HttpResponse
from .models import brand,product
from .forms import ProductCreateForm,BrandCreateForm
from django.views.generic import (
ListView,
CreateView,
DetailView,
UpdateView,
DeleteView)
from django.contrib.auth.models import User 

# Create your views here.

def index(request):
    return render(request,"finder/index.html",{})

def about(request):
    return render(request,"finder/about.html",{})

def reviewers(request):
    #if request.method == "POST":
    newform=ProductCreateForm()

    if request.method == "POST":
        newform=ProductCreateForm(request.POST)
        if newform.is_valid():
            newform.save()
    


    return render(request,"finder/product_form.html",{"form":newform})

def branders(request):
    #if request.method == "POST":
    form=BrandCreateForm()
    if request.method != "GET":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"finder/brand_form.html",{"form":form})


class BrandListView(ListView):
        # model=brand
        queryset=brand.objects.order_by('position')
        template_name="finder/brand_list.html"
        context_object_name="brands"

class ProdLsView(ListView):
        queryset=list(product.objects.order_by('rating'))[::-1]
        template_name="finder/ProductList_Trending.html"
        context_object_name="products"

def signup(request):
    if (request.method=='POST'):
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        User.objects.create_user(username,email,password)
    return render(request,"finder/loginform.html",{})