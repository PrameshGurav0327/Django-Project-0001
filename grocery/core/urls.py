from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("products/",views.products,name='products'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name="contact"),
    path("product_details/",views.product_details,name="product_details"),
    path("cart/",views.cart,name="cart"),
]
