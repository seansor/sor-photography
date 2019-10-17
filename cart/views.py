from django.shortcuts import render, redirect, reverse

import os
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

def view_cart(request):
    """
    Returns all of the contents of the cart
    """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """
    Allows users to add items to cart
    """
    quantity = int(request.POST.get('quantity'))
    product_variant_id = request.POST.get('size-select')
    
    logger.debug(product_variant_id)
    
    cart = request.session.get('cart', {})
    if product_variant_id in cart:
        cart[product_variant_id] = int(cart[product_variant_id]) +  quantity
    else:
        cart[product_variant_id] = cart.get(product_variant_id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
 
    
def edit_cart(request, id):
    """
    edit the quantity of a product in the cart
    """
    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[id] = quantity
        else:
            cart.pop(id)
        request.session['cart'] = cart
    else:
        return redirect(reverse('view_cart'))
        
    return redirect(reverse('view_cart'))