from django.shortcuts import render
from .models import Product, ProductVariant
import os
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products })


def product(request, id):
    product = Product.objects.get(id=id)
    product_variants = ProductVariant.objects.all()
    logger.warning(product_variants)
    #price_of_each_size = zip(product_variants.size, product_variants.price)
    return render(request, 'product.html', {'product': product, 'product_variants': product_variants})