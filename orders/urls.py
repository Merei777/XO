from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='orders_home'),
    path('create/', views.create_order, name='create_order'),
    path('cart/add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('success/', views.order_success, name='order_success'),
]
