from django.contrib import admin

from django.contrib import admin
from EShop.models import Category, Brand, Product, CartItem, Cart, Order

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)