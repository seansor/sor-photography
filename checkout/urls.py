from django.conf.urls import url
from .views import checkout, commission_checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^commission_checkout/(?P<id>\d+)$', commission_checkout, name='commission_checkout'),
]