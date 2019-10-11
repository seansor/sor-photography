from django.shortcuts import render
from .models import Collection, Product, ProductVariant
import os
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

def all_products(request):
    #current_series = Product.objects.get(collection="Pubs of Dublin")
    products = Product.objects.all()
    collections = Collection.objects.all()
    collection_ids = []
    collection_images = []
    for collection in collections:
        product = Product.objects.filter(collection_id=collection.id).first()
        collection_image = product.image
        collection_images.append(collection_image)
        collection_id = product.collection_id
        collection_ids.append(collection_id)
    logger.debug(collection_images)
    logger.debug(collection_ids)
    collections = Collection.objects.values()
    current_series = Collection.objects.get(current_series=True)
    return render(request, 'products.html', {'products': products,  'current_series': current_series, 'collections': collections })


def product(request, id):
    product = Product.objects.get(id=id)
    product_variants = list(ProductVariant.objects.values())
    logger.info(product_variants)
    #price_of_each_size = zip(product_variants.size, product_variants.price)
    return render(request, 'product.html', {'product': product, 'product_variants': product_variants})