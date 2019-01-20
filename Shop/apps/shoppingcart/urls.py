from django.conf.urls import url

from shoppingcart.views import shopcart

urlpatterns = [
    url(r'^shopcart/$', shopcart, name='购物车'),
]