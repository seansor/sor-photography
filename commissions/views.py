from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from .forms import OrderForm
from .models import CommissionOrder, Quote

# Create your views here.

def create_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.client_id = "test"
            # process the data in form.cleaned_data as required
            order = order_form.save(commit=False)
            order.client = request.user
            order.date = timezone.now()
            order.save()
            
            messages.error(request, "Your request has been sent successfully.")
            return redirect(reverse('products'))
            # redirect to a new URL:
    else:
        form = OrderForm()
        
    return render(request, 'order.html', {'order_form': form})
        
