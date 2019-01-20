from django.conf.urls import url

from user.views import RegisterView, LoginView, message, member, step

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='注册'),
    url(r'^login/$', LoginView.as_view(), name='登录'),
    url(r'^message/$', message, name='动态'),
    url(r'^member/$', member, name='我的详情'),
    url(r'^step/$', step, name='系统设置'),
]
