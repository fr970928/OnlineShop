from django.conf.urls import url

from order.views import allorder

urlpatterns = [
    url(r'^allorder/$', allorder, name='订单'),
]