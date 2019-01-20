from django.shortcuts import render, redirect
from Shop.user.models import Users
# Create your views here.
from django.views import View
from Shop.user.forms import RegisterModelForm, LoginModelForm
from Shop.user import set_password


# 定义注册页面的视图类
class RegisterView(View):

    def get(self, request):
        # 跳转注册表单
        return render(request, 'user/reg.html')

    def post(self, request):  # 注册页面视图
        # 接收参数
        data = request.POST
        # 表单验证合法
        form = RegisterModelForm(data)
        if form.is_valid():
            # 操作数据库
            clened_data = form.cleaned_data
            # 创建一个用户
            user = Users()
            user.user_name = clened_data.get('user_name')
            user.password = set_password(clened_data.get('password'))
            user.save()
            return redirect('user:登录')
        # 错误
        else:
            return render(request, 'user/login.html', context={'form': form})


# 定义登录页面的视图类
class LoginView(View):
    def get(self, request):
        # 跳转登录页面
        return render(request, 'user/login.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 表单验证合法
        form = LoginModelForm(data)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            request.session['ID'] = user.pk
            request.session['user_name'] = user.user_name
            return redirect('item:主页')
        else:
            return render(request, 'user/login.html', context={'form': form})
