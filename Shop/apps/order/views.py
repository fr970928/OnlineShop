from django.shortcuts import render

# Create your views here.


# 确认订单
def tureorder(request):
    return render(request, 'order/tureorder.html')


# 全部订单
def allorder(request):
    return render(request, 'order/allorder.html')
