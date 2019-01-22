from django.shortcuts import render, redirect
from user.models import Users, Address
# Create your views here.
from django.views import View
from user.forms import RegisterModelForm, LoginModelForm, InforModelForm, AddressModelForm
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


# 个人资料
def infor(request):
    # 查询数据库
    data = Users.objects.all()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'user/infor.html', context=context)


# 修改个人资料
class AddinfoView(View):
    def get(self, request):
        # 跳转编辑个人资料页面
        return render(request, 'user/addinfor.html')

    def post(self, request):
        # 接受参数
        data = request.POST
        user = Users.objects.get(pk=1)
        # 表单验证合法
        form = InforModelForm(data, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:收货地址')
        else:
            # 提示错误
            context = {
                'form': form
            }
            return render(request, 'user/addinfor.html', context=context)

# 关于我们
def about(request):
    return render(request, 'user/about.html')


# 账户余额
def records(request):
    return render(request, 'user/records.html')


# 积分
def integral(request):
    return render(request, 'user/integral.html')


# 积分兑换
def integralexchange(request):
    return render(request, 'user/integralexchange.html')


# 兑换记录
def integralrecords(request):
    return render(request, 'user/integralrecords.html')


# 我的收藏
def collect(request):
    return render(request, 'user/collect.html')


# 我的收藏编辑
def collect_edit(request):
    return render(request, 'user/collect-edit.html')


# 收货地址
def gladdress(request):
    # 查询数据库
    data = Address.objects.all()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'user/gladdress.html', context=context)


# 新增收货地址
class AddressView(View):
    def get(self, request):
        # 跳转增加收货地址表单
        return render(request, 'user/address.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 表单验证合法
        form = AddressModelForm(data)
        if form.is_valid():
            form.save()
            return redirect('user:收货地址')
        # 错误
        else:
            return render(request, 'user/address.html', context={'form': form})


# 安全设置
def saftystep(request):
    return render(request, 'user/saftystep.html')


# 修改密码
def password(request):
    return render(request, 'user/password.html')


# 支付密码
def payment(request):
    return render(request, 'user/payment.html')


# 绑定手机
def boundphone(request):
    return render(request, 'user/boundphone.html')


# 我的钱包
def money(request):
    return render(request, 'user/money.html')


# 我要兼职
def job(request):
    return render(request, 'user/job.html')


# 兼职申请记录
def application(request):
    return render(request, 'user/application.html')


# 申请兼职
def applicationjob(request):
    return render(request, 'user/applicationjob.html')


# 推荐有奖
def recommend(request):
    return render(request, 'user/recommend.html')


# 我的推荐
def myrecommend(request):
    return render(request, 'user/myrecommend.html')
