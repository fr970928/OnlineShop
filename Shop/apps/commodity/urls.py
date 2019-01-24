from django.conf.urls import url

from commodity.views import commodity_list, comcategory, index, city, village, tidings, recharge, yhq, ygq, speed, \
    s_list, detail, category

urlpatterns = [
    url('^index/$', index, name='首页'),
    url('^city/$', city, name='城市选择'),
    url('^village/$', village, name='校区选择'),
    url('^tidings/$', tidings, name='消息中心'),
    url('^recharge/$', recharge, name='充值'),
    url('^yhq/$', yhq, name='红包'),
    url('^ygq/$', ygq, name='过期红包'),
    url('^speed/$', speed, name='零食飞速'),
    url('^slist/$', s_list, name='琳琅的店'),
    url('^detail/(?P<id>\d+)/$', detail, name='商品详情'),
    url('^category/(?P<cate_id>\d*)_{1}(?P<order>\d?)\.html$', category, name='超市'),
    url('^commodity_list/$', commodity_list, name='商品列表'),
    url('^comcategory/$', comcategory, name='商品分类'),
]
