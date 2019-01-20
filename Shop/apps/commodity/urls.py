from django.conf.urls import url

from commodity.views import commodity_list, comcategory, index

urlpatterns = [
    url('^index/$', index, name='首页'),
    url('^commodity_list/$', commodity_list, name='商品列表'),
    url('^comcategory/$', comcategory, name='商品分类'),
]
