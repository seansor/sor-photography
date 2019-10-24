from django import forms
from django.contrib.auth.models import User
from .models import CommissionOrder, Quote


class OrderForm(forms.ModelForm):
    """Order form to request commissions"""
    
    class Meta:
        model = CommissionOrder
        exclude = ['customer', 'date']
        
class QuoteForm(forms.ModelForm):
    """Quote form to for requested commissions"""
    
    class Meta:
        model = Quote
        exclude = ['price_total', 'date', 'accepted', 'rejected']