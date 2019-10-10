from django.shortcuts import render, redirect, reverse

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
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) +  quantity
    else:
        cart[id] = cart.get(id, quantity)
    
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