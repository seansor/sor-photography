from django.conf.urls import url, include
from .views import create_order, get_orders, reject_quote, create_quote

urlpatterns = [
     url(r'^create_order/$', create_order, name="create_order"),
     url(r'^orders/$', get_orders, name="get_orders"),
     url(r'^create_quote/(?P<order_id>\d+)$', create_quote, name='create_quote'),
     url(r'^reject_quote/(?P<quote_id>\d+)$', reject_quote, name='reject_quote'),
]