
from django.shortcuts import render

# Create your views here.


# 购物车
def shopcart(request):
    return render(request, 'shoppingcart/shopcart.html')
