from django.contrib import admin
from .models import OrderBillingInfo, OrderLineItem

# Register your models here.

class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem
    
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    

admin.site.register(OrderBillingInfo, OrderAdmin)