from django.shortcuts import render
from .models import Collection, Product, ProductVariant

# Create your views here.

def all_products(request):
    """ Render Index Page """
    # If user is not logged in set session to expire on logout
    if not request.user.is_authenticated:
        request.session.set_expiry(0)

    products = Product.objects.all()
    collections = Collection.objects.all()

    # Set thumbnails for featured collections to first image in collection
    first_product_ids = []
    collection_ids = []
    collection_images = []
    collection_image_names = []
    collection_names = []
    for collection in collections:
        first_product = Product.objects.filter(collection=collection).first()
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

    collection_details = zip(first_product_ids, collection_ids, collection_images,
                             collection_image_names, collection_names)
    current_series = Collection.objects.get(current_series=True)

    return render(request, 'products.html', {'products': products,
                                             'current_series': current_series,
                                             'collections': collections,
                                             'collection_details': collection_details})


def product(request, product_id):
    """ Render Individual Product Page"""
    product = Product.objects.get(id=product_id)
    product_variants = ProductVariant.objects.filter(product_id=product_id)

    return render(request, 'product.html',
                  {'product': product, 'product_variants': product_variants})
