from django.contrib import admin
from .models import Quote, CommissionOrder

# Register your models here.

# class CommissionOrderAdminInline(admin.TabularInline):
#     model = CommissionOrder
    
    
# class CommissionOrderAdmin(admin.ModelAdmin):
#     inlines = [CommissionOrderAdminInline, ]
    
    
admin.site.register(CommissionOrder)
    
admin.site.register(Quote)

