from django.conf.urls import url, include
from .views import create_order, get_orders, reject_quote

urlpatterns = [
     url(r'^create_order/$', create_order, name="create_order"),
     url(r'^orders/$', get_orders, name="get_orders"),
     url(r'^reject_quote/(?P<id>\d+)$', reject_quote, name='reject_quote'),
]