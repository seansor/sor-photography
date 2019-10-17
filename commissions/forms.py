from django import forms
from django.contrib.auth.models import User
from .models import CommissionOrder


class OrderForm(forms.ModelForm):
    """Order form to request commissions"""
    
    class Meta:
        model = CommissionOrder
        fields = ('description', 'size', 'location')