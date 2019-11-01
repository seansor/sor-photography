from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import OrderForm, QuoteForm
from .models import CommissionOrder, Quote


# Create your views here.

@login_required()
def create_order(request):
    """ Create Commission Order """
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # process the data in form.cleaned_data as required
            order = order_form.save(commit=False)
            order.customer_id = request.user.id
            order.date = timezone.now()
            order.save()

            messages.success(request, "Your request has been sent successfully.")
            return redirect(reverse('products'))
    else:
        order_form = OrderForm()

    return render(request, 'order.html', {'order_form': order_form})


@login_required()
def get_orders(request):
    """ Render Page with all commission orders """
    orders = CommissionOrder.objects.all()
    return render(request, 'orders.html', {'orders': orders})


@login_required()
def create_quote(request, order_id):
    """ Create 'Quote' (price proposal) for requested commission """
    commission_order = CommissionOrder.objects.get(pk=order_id)
    if request.method == 'POST':
        quote_form = QuoteForm(request.POST)
        if quote_form.is_valid():
            quote = quote_form.save(commit=False)
            quote.order = commission_order
            quote.date = timezone.now()
            quote.save()
            messages.success(request, "Quote successfully sent")
            return redirect(reverse('get_orders'))
    else:
        quote_form = QuoteForm()

    return render(request, 'quote.html',
                  {'commission_order': commission_order, 'quote_form': quote_form})


@login_required()
def reject_quote(request, quote_id):
    """ Allow user to reject quote """
    quote = Quote.objects.get(pk=quote_id)
    quote.rejected = True
    quote.save()

    return redirect(reverse('profile'))
