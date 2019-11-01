from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
import stripe
from products.models import ProductVariant
from commissions.models import Quote
from .forms import MakePaymentForm, OrderForm
from .models import OrderInfo, OrderLineItem


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()
def checkout(request):
    """ Customer checkout for purchasing products in cart """

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        # Save order information/details
        if order_form.is_valid() and payment_form.is_valid():
            order_info = order_form.save(commit=False)
            order_info.customer_id = request.user.id
            order_info.date = timezone.now()
            order_info.save()

            # Save order line items
            cart = request.session.get('cart', {})
            total = 0
            for product_variant_id, quantity in cart.items():
                product_variant = get_object_or_404(ProductVariant, pk=product_variant_id)
                total += quantity * product_variant.price
                order_line_item = OrderLineItem(
                    order_info=order_info,
                    product_variant=product_variant,
                    quantity=quantity,
                    line_total=product_variant.price * quantity)

                order_line_item.save()

            # Stripe payment
            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            # If payment successful empty cart and redirect
            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card")
    else:
        # Get cart object from contexts
        cart = request.session.get('cart')

        # Create payment form
        payment_form = MakePaymentForm()

        current_user = request.user.id

        try:
            # If user has remember me set on last purchase fill in billing/shipping details
            billing_info = OrderInfo.objects.filter(customer_id=current_user).latest('id')
            if billing_info.remember_me:
                order_form = OrderForm(initial={'full_name': billing_info.full_name,
                                                'phone_number': billing_info.phone_number,
                                                'country': billing_info.country,
                                                'postcode': billing_info.postcode,
                                                'town_or_city': billing_info.town_or_city,
                                                'street_address1': billing_info.street_address1,
                                                'street_address2': billing_info.street_address2,
                                                'county': billing_info.county,
                                                'remember_me': billing_info.remember_me
                                                })
            else:
                order_form = OrderForm()
        except:
            order_form = OrderForm()
    return render(request, 'checkout.html', {'order_form': order_form,
                                             'payment_form': payment_form,
                                             'publishable': settings.STRIPE_PUBLISHABLE_KEY})


@login_required()
def commission_checkout(request, quote_id):
    """ Checkout for user purchasing commission work """

    quote = Quote.objects.get(pk=quote_id)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            total = quote.price_total
            # Stripe Payment
            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            # If payment is accepted change "quote.accepted" status and
            # redirect to products
            if customer.paid:
                messages.success(request, "You have successfully paid")
                quote.accepted = True
                quote.save()
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card")
    else:
        payment_form = MakePaymentForm()
        current_user = request.user.id

        try:
            # If user has remember me set on last purchase fill in billing/shipping details
            billing_info = OrderInfo.objects.filter(customer_id=current_user).latest('id')
            if billing_info.remember_me:
                order_form = OrderForm(initial={'full_name': billing_info.full_name,
                                                'phone_number': billing_info.phone_number,
                                                'country': billing_info.country,
                                                'postcode': billing_info.postcode,
                                                'town_or_city': billing_info.town_or_city,
                                                'street_address1': billing_info.street_address1,
                                                'street_address2': billing_info.street_address2,
                                                'county': billing_info.county,
                                                'remember_me': billing_info.remember_me
                                                })
            else:
                order_form = OrderForm()
        except:
            order_form = OrderForm()

    return render(request, 'comm_checkout.html', {'quote': quote, 'order_form': order_form,
                                                  'payment_form': payment_form,
                                                  'publishable': settings.STRIPE_PUBLISHABLE_KEY})
    