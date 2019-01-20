from django.conf.urls import url

from order.views import tureorder, allorder

urlpatterns = [
   url(r'tureorder', tureorder, name='确认订单'),
   url(r'allorder', allorder, name='全部订单'),
]
