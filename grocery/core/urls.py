from django.urls import path
from . import views

#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path("products/",views.products,name='products'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name="contact"),
    path("product_details/",views.product_details,name="product_details"),
    path("cart/",views.cart,name="cart"),
    path("view_cart/",views.view_cart,name="view_cart"),
    path('foodcategories/',views.foodcategories,name='foodcategories'),
    path('kitchencategories/',views.kitchencategories,name='kitchencategories'),
    path('instantfoodcategories/',views.instantfoodcategories,name='instantfoodcategories'),
    path('fruitscategories/',views.fruitscategories,name='fruitscategories'),
]