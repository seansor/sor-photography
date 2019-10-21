from django.shortcuts import get_object_or_404
from .models import Quote

def user_quotes(request):
    
    quotes = Quote.objects.filter(order__customer=request.user.id)
    
    quotes_count = quotes.count()

    return { 'quotes_count': quotes_count}