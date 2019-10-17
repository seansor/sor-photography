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
    
    for product_variant_id, quantity in cart.items():
        product_variant = get_object_or_404(ProductVariant, pk=product_variant_id)
        total += quantity * product_variant.price
        product_count += quantity
        cart_items.append({'id':product_variant_id, 'quantity': quantity, 'product': product_variant.product})
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }