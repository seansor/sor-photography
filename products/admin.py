from django.contrib import admin
from .models import Collection, Product, ProductVariant

# Register your models here.

class ProductVariantAdminInline(admin.TabularInline):
    model = ProductVariant
    
    
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductVariantAdminInline, ]
    
    
admin.site.register(Product, ProductVariantAdmin)

admin.site.register(Collection)


