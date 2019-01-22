from django.shortcuts import render
from user.helper import check_login

# Create your views here.


# 首页
@check_login
def index(request):
    return render(request, 'commodity/index.html')


# 首页左上城市选择
@check_login
def city(request):
    return render(request, 'commodity/city.html')


# 首页校区选择
@check_login
def village(request):
    return render(request, 'commodity/village.html')


# 首页消息中心
@check_login
def tidings(request):
    return render(request, 'commodity/tidings.html')


# 首页充值
@check_login
def recharge(request):
    return render(request, 'commodity/recharge.html')


# 首页红包
@check_login
def yhq(request):
    return render(request, 'commodity/yhq.html')


# 过期红包
@check_login
def ygq(request):
    return render(request, 'commodity/ygq.html')


# 首页零食飞速
@check_login
def speed(request):
    return render(request, 'commodity/speed.html')


# 飞速零食中七米设计零食屋
@check_login
def s_list(request):
    return render(request, 'commodity/list.html')


# 商品详情
@check_login
def detail(request):
    return render(request, 'commodity/detail.html')


# 超市
@check_login
def category(request):
    return render(request, 'commodity/category.html')


# 商品列表
@check_login
def commodity_list(request):
    return render(request, 'commodity/list.html')


# 商品分类
@check_login
def comcategory(request):
    return render(request, 'commodity/category.html')
