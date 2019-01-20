from django.shortcuts import render


# Create your views here.
# 首页
def index(request):
    return render(request, 'commodity/index.html')


# 首页左上城市选择
def city(request):
    return render(request, 'commodity/city.html')


# 首页校区选择
def village(request):
    return render(request, 'commodity/village.html')


# 首页消息中心
def tidings(request):
    return render(request, 'commodity/tidings.html')


# 首页充值
def recharge(request):
    return render(request, 'commodity/recharge.html')


# 首页红包
def yhq(request):
    return render(request, 'commodity/yhq.html')


# 过期红包
def ygq(request):
    return render(request, 'commodity/ygq.html')


# 首页零食飞速
def speed(request):
    return render(request, 'commodity/speed.html')


# 飞速零食中七米设计零食屋
def s_list(request):
    return render(request, 'commodity/list.html')


# 商品详情
def detail(request):
    return render(request, 'commodity/detail.html')


# 超市
def category(request):
    return render(request, 'commodity/category.html')


# 商品列表
def commodity_list(request):
    return render(request, 'commodity/list.html')


# 商品分类
def comcategory(request):
    return render(request, 'commodity/category.html')
