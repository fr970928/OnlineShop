from django.shortcuts import render
from user.helper import check_login
# Create your views here.


# 确认订单
@check_login
def tureorder(request):
    return render(request, 'order/tureorder.html')


# 全部订单
@check_login
def allorder(request):
    return render(request, 'order/allorder.html')
