from django.shortcuts import render

from commodity.models import GoodsClassifyModel, BannerModel, GoodsSkuModel
from user.helper import check_login

# Create your views here.


# 首页
def index(request):
    banner = BannerModel.objects.all()
    data = GoodsSkuModel.objects.all()
    context = {
        'banner': banner,
        "data": data
    }
    return render(request, 'commodity/index.html', context=context)


# 首页左上城市选择
def city(request):
    return render(request, 'commodity/city.html')


# 首页校区选择
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
def speed(request):
    return render(request, 'commodity/speed.html')


# 飞速零食中七米设计零食屋
def s_list(request):
    return render(request, 'commodity/list.html')


# 商品详情
def detail(request, id):
    data = GoodsSkuModel.objects.get(pk=id)
    context = {
        'data': data
    }
    return render(request, 'commodity/detail.html', context=context)


# 超市
def category(request):
    # 查询分类名称
    classify = GoodsClassifyModel.objects.all()
    # 查询商品SKU详情
    data = GoodsSkuModel.objects.all()
    context = {
        'classify': classify,
        'data': data
    }
    return render(request, 'commodity/category.html', context=context)


# 商品列表
def commodity_list(request):
    return render(request, 'commodity/list.html')


# 商品分类
def comcategory(request):
    return render(request, 'commodity/category.html')
