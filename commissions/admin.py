from django.contrib import admin
from .models import Quote, CommissionOrder

# Register your models here.
    
admin.site.register(CommissionOrder)
    
admin.site.register(Quote)

