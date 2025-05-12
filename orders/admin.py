from django.contrib import admin
from .models import Order, OrderItem, ShippingInfo

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class ShippingInfoInline(admin.StackedInline):
    model = ShippingInfo

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'is_paid')
    list_filter = ('is_paid', 'created_at')
    inlines = [OrderItemInline, ShippingInfoInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')

@admin.register(ShippingInfo)
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ('order', 'full_name', 'city', 'country')
