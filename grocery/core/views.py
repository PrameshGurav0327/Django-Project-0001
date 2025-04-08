from django.shortcuts import render,redirect,get_object_or_404
from . models import Grocery, Cart
from . forms import RegistrationForm,AuthenticateForm,ChangePasswordForm,UserProfileForm,AdminProfileForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def products(request):
    return render(request,'core/products.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

def cart(request):
    return render(request,'core/cart.html')

def view_cart(request):
    return render(request,'core/view_cart.html')

def foodcategories(request):
    return render(request,"core/foodcategories.html")

def fruitscategories(request):
    return render(request,"core/fruitscategories.html")

def kitchencategories(request):
    return render(request,"core/kitchencategories.html")

def instantfoodcategories(request):
    return render(request,"core/instantfoodcategories.html")

def product_details(request, id):
    GC = get_object_or_404(Grocery, pk=id)
    return render(request, '../core/product_details.html', {'GC': GC})

# =============== Add to cart and Delete item ==============

def add_to_cart(request,id):
    if request.user.is_authenticated:
        pet = Grocery.objects.get(pk=id)
        user = request.user
        Cart(user=user,product=pet).save()
        messages.success(request,'Added to cart succcefully !')
        return redirect('petdetails', id)
    else:
        return redirect('login')


def view_cart(request):
    if request.user.is_authenticated:
        cart_items =Cart.objects.filter(user=request.user)
        total=0
        delhivery_charge=2000
        for item in cart_items:
            total+=(item.product.discounted_price*item.quantity)
        final_price =total+delhivery_charge
        return render(request,'core/view_cart.html',{'cart_items':cart_items,'total':total,'final_price':final_price})
    else:
        return redirect('login')


def add_quantity(request,id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart,pk=id)
        product.quantity+=1
        product.save()
        return redirect('viewcart')
    else:
        return redirect('login')

def delete_quantity(request,id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart,pk=id)
        if product.quantity>1:
            product.quantity-=1
            product.save()
        return redirect('viewcart')
    else:
        return redirect('login')
    
def delete_cart(request,id):
    pet_cart =Cart.objects.get(pk=id)
    pet_cart.delete()
    return redirect('viewcart')

