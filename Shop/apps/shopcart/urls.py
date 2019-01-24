from django.conf.urls import url

from shopcart.views import shopcart

urlpatterns = [
    url('^shopcart/$', shopcart, name='购物车')
]
