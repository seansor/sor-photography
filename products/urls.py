from django.conf.urls import url, include
from .views import all_products, product

urlpatterns = [
     url(r'^$', all_products, name="products"),
     url(r'^(?P<product_id>\d+)', product, name="product" ),
]