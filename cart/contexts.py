from django.shortcuts import get_object_or_404
from products.models import Product, ProductVariant

def cart_contents(request):
    """
    Ensures cart contents are available on every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    
    for id, quantity in cart.items():
        product_variant = get_object_or_404(ProductVariant, pk=id)
        item_total = quantity * product_variant.price
        total += quantity * product_variant.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'item_total': item_total, 'product_variant': product_variant})
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }