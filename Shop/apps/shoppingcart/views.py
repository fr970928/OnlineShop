from user.helper import check_login
from django.shortcuts import render

# Create your views here.


# 购物车


@check_login
def shopcart(request):
    return render(request, 'shoppingcart/shopcart.html')
