from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product, ProductVariant


# Create your views here.

def view_cart(request):
    """
    Returns all of the contents of the cart
    """
    return render(request, "cart.html")


def add_to_cart(request, product_id):
    """
    Allows users to add items to cart
    """
    try:
        quantity = int(request.POST.get('quantity'))
        product_variant_id = request.POST.get('size-select')
    except:
        messages.warning(request, "Please select a size and quantity")
        product = Product.objects.get(id=product_id)
        product_variants = ProductVariant.objects.filter(product_id=product_id)

        return render(request, 'product.html', {'product': product,
                                                'product_variants': product_variants})

    cart = request.session.get('cart', {})

    if product_variant_id in cart:
        cart[product_variant_id] = int(cart[product_variant_id]) +  quantity
    else:
        cart[product_variant_id] = cart.get(product_variant_id, quantity)

    request.session['cart'] = cart

    messages.success(request, "Product successfully added to cart.")

    return redirect(reverse('index'))


def edit_cart(request, product_variant_id):
    """
    edit the quantity of a product in the cart
    """
    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        if quantity > 0:
            cart[product_variant_id] = quantity
        else:
            cart.pop(product_variant_id)
        request.session['cart'] = cart
    else:
        return redirect(reverse('view_cart'))

    return redirect(reverse('view_cart'))
