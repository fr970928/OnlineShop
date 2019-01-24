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
def category(request, cate_id, order):
    # 查询分类名称
    classify = GoodsClassifyModel.objects.filter(is_delete=False).order_by('-order')
    # 查询第一个分类
    if cate_id == '':
        data = classify.first()
        cate_id = data.pk
    else:
        # 根据分类id查询对应的分类
        cate_id = int(cate_id)
        data = GoodsClassifyModel.objects.get(pk=cate_id)
    # 查询对应分类下所有的商品
    goods = GoodsSkuModel.objects.filter(is_delete=False, goods_cate=data)
    # 查询商品SKU详情
    # data = GoodsSkuModel.objects.all()
    # 排序
    if order == '':
        order = 0
    order = int(order)
    # if order == 0:
    #     goods = goods.order_by("pk")
    # elif order == 1:
    #     goods = goods.order_by("-sell_num")
    # elif order == 2:
    #     goods = goods.order_by("price")
    # elif order == 3:
    #     goods = goods.order_by("-price")
    # elif order == 4:
    #     goods = goods.order_by("-create_time")

    # 排序规则列表
    order_rule = ['pk', '-sell_num', 'price', '-price', '-create_time']
    goods = goods.order_by(order_rule[order])
    context = {
        'classify': classify,
        'goods': goods,
        'cate_id': cate_id,
        'order': order,
    }
    return render(request, 'commodity/category.html', context=context)


# 商品列表
def commodity_list(request):
    return render(request, 'commodity/list.html')


# 商品分类
def comcategory(request):
    return render(request, 'commodity/category.html')
