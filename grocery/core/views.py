from django.shortcuts import render,redirect,get_object_or_404
from django.views import View

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def products(request):
    return render(request,'core/products.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

def product_details(request):
    return render(request,'core/product_details.html')

def cart(request):
    return render(request,'core/cart.html')

def view_cart(request):
    return render(request,'core/view_cart.html')

