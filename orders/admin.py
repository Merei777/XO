from django.contrib import admin
from .models import OrderStatus, PaymentMethod, DeliveryAddress, Order, OrderItem

admin.site.register(OrderStatus)
admin.site.register(PaymentMethod)

@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line', 'city', 'postal_code', 'country')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ('id', 'user', 'status', 'payment_method', 'total_price', 'created_at')
    list_filter   = ('status', 'payment_method', 'created_at')
    search_fields = ('user__email',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity', 'price')
