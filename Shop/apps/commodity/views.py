from django.shortcuts import render


# Create your views here.
# 首页
def index(request):
    return render(request, 'commodity/index.html')

# 商品列表
def commodity_list(request):
    return render(request, 'commodity/list.html')


# 商品分类
def comcategory(request):
    return render(request, 'commodity/category.html')
