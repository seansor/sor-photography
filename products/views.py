from django.shortcuts import render
from .models import Collection, Product, ProductVariant
import os
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    collections = Collection.objects.all()
    first_product_ids = []
    collection_ids = []
    collection_images = []
    collection_image_names = []
    collection_names = []
    for collection in collections:
        first_product = Product.objects.filter(collection_id=collection.id).first()
        first_product_id = first_product.id
        first_product_ids.append(first_product_id)
        collection_id = first_product.collection_id
        collection_ids.append(collection_id)
        collection_image = first_product.image
        collection_images.append(collection_image)
        collection_image_name = first_product.name + ', ' + first_product.location
        collection_image_names.append(collection_image_name)
        collection_name = collection.name
        collection_names.append(collection_name)
    
    collection_details = zip(first_product_ids, collection_ids, collection_images, collection_image_names, collection_names)
    current_series = Collection.objects.get(current_series=True)
    return render(request, 'products.html', {'products': products,  'current_series': current_series,
                'collections': collections, 'collection_details':  collection_details})


def product(request, id):
    product = Product.objects.get(id=id)
    product_variants = ProductVariant.objects.filter(product_id=id)
    #product_variants = list(ProductVariant.objects.values(product_id=id))
    #price_of_each_size = zip(product_variants.size, product_variants.price)
    return render(request, 'product.html', {'product': product, 'product_variants': product_variants})