from django.shortcuts import render, redirect
from user.models import Users
# Create your views here.
from django.views import View
from user.forms import RegisterModelForm, LoginModelForm
from user import set_password


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
            user.phone = clened_data.get('phone')
            user.password = set_password(clened_data.get('password'))
            user.save()
            return redirect('user:登录')
        # 错误
        else:
            return render(request, 'user/reg.html', context={'form': form})


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
            request.session['phone'] = user.phone
            return redirect('com:首页')
        else:
            return render(request, 'user/login.html', context={'form': form})


# 动态
def message(request):
    return render(request, 'user/message.html')


# 我的详情
def member(request):
    return render(request, 'user/member.html')


# 系统设置
def step(request):
    return render(request, 'user/step.html')


