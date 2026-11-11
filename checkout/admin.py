from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)
    list_display = ('order_number', 'user', 'status', 'total', 'created_on')
    list_filter = ('status',)
    readonly_fields = ('order_number', 'total', 'created_on')
