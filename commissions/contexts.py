from django.shortcuts import get_object_or_404
from .models import Quote

def user_quotes(request):
    
    quotes = Quote.objects.filter(order__customer=request.user.id)
    
    count = 0
    for quote in quotes:
        if quote.rejected == False and quote.accepted == False:
            count += 1

    return { 'count': count}