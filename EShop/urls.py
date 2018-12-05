from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from EShop.views import (
	base_view, 
	product_view, 
	category_view, 
	cart_view, 
	add_to_cart_view, 
	remove_from_cart_view, 
	change_item_qty,
	checkout_view,
	order_create_view,
	make_order_view,
	account_view,
	registration_view,
	login_view
	)
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', base_view, name = 'base'),
    re_path(r'^product/(?P<product_slug>[\w-]+)/$', product_view, name = 'product_detail'),
    re_path(r'^category/(?P<category_slug>[\w-]+)/$', category_view, name = 'category_detail'),
    path('cart/', cart_view, name = 'cart'),
    path('checkout/', checkout_view, name = 'checkout'),
    path('order/', order_create_view, name = 'create_order'),
    path('make_order/', make_order_view, name = 'make_order'),
    path('thank_you/', TemplateView.as_view(template_name = 'thank_you.html'), name = 'thank_you'),
    path('account/', account_view, name = 'account'),
    path('registration/', registration_view, name = 'registration'),
    path('login/', login_view, name = 'login'),
    path('logout/', LogoutView.as_view(next_page = reverse_lazy('base')), name = 'logout'),
	re_path(r'^change_item_qty/$', change_item_qty, name = 'change_item_qty'),
	re_path(r'^add_to_cart/$', add_to_cart_view, name = 'add_to_cart'),
    re_path(r'^remove_from_cart/$', remove_from_cart_view, name = 'remove_from_cart'),
]