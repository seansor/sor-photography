from django.contrib import admin
from .models import Quote, CommissionOrder

# Register your models here.

admin.site.register(Quote)
admin.site.register(CommissionOrder)