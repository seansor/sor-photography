from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.utils import timezone
from .forms import OrderForm
from .models import CommissionOrder, Quote

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

def create_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # process the data in form.cleaned_data as required
            order = order_form.save(commit=False)
            order.customer_id = request.user.id
            order.date = timezone.now()
            order.save()
            
            messages.error(request, "Your request has been sent successfully.")
            return redirect(reverse('products'))
            # redirect to a new URL:
    else:
        #CommissionOrder.objects.all().delete()
        order_form = OrderForm()
        
    return render(request, 'order.html', {'order_form': order_form})
        

def get_orders(request):
    orders = CommissionOrder.objects.all()
    
    return render(request, 'orders.html', {'orders': orders})
