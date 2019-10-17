from django.conf.urls import url, include
from .views import create_order

urlpatterns = [
     url(r'^order/$', create_order, name="order"),
     # url(r'^(?P<id>\d+)', product, name="product" ),
]