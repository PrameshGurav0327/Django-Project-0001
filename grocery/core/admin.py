from django.contrib import admin
from .models import CustomerDetail,Cart,Order,Grocery

# Register your models here.

@admin.register(CustomerDetail)
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['id','user','name','address','city','state','pincode']


@admin.register(Grocery)
class productAdmin(admin.ModelAdmin):
    list_display= ['id','name','category','small_description','description','original_price','discounted_price']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ['id','user','customer','pet','quantity','order_at','status','total_price']
