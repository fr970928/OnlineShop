from django.conf.urls import url

from user.views import RegisterView, LoginView, message, member, step, infor, about, records, integral, \
    integralexchange, integralrecords, collect, collect_edit, gladdress, saftystep, password, payment, \
    boundphone, money, job, application, applicationjob, recommend, myrecommend, AddinfoView, AddressView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='注册'),
    url(r'^login/$', LoginView.as_view(), name='登录'),
    url(r'^message/$', message, name='动态'),
    url(r'^member/$', member, name='我的详情'),
    url(r'^step/$', step, name='系统设置'),
    url(r'^infor/$', infor, name='个人资料'),
    url(r'^addinfor/$', AddinfoView.as_view(), name='修改个人资料'),
    url(r'^about/$', about, name='关于我们'),
    url(r'^records/$', records, name='账户余额'),
    url(r'^integral/$', integral, name='积分'),
    url(r'^integralexchange/$', integralexchange, name='积分兑换'),
    url(r'^integralrecords/$', integralrecords, name='兑换记录'),
    url(r'^collect/$', collect, name='我的收藏'),
    url(r'^collect_edit/$', collect_edit, name='我的收藏编辑'),
    url(r'^gladdress/$', gladdress, name='收货地址'),
    url(r'^address/$', AddressView.as_view(), name='新增收货地址'),
    url(r'^saftystep/$', saftystep, name='安全设置'),
    url(r'^password/$', password, name='修改密码'),
    url(r'^payment/$', payment, name='支付密码'),
    url(r'^boundphone/$', boundphone, name='绑定手机'),
    url(r'^money/$', money, name='我的钱包'),
    url(r'^job/$', job, name='我要兼职'),
    url(r'^application/$', application, name='兼职申请记录'),
    url(r'^applicationjob/$', applicationjob, name='申请兼职'),
    url(r'^recommend/$', recommend, name='推荐有奖'),
    url(r'^myrecommend/$', myrecommend, name='我的推荐'),
]
