from django.conf.urls import url, include
from .views import create_order, get_orders

urlpatterns = [
     url(r'^create_order/$', create_order, name="create_order"),
     url(r'^orders/$', get_orders, name="get_orders"),
     # url(r'^(?P<id>\d+)', product, name="product" ),
]