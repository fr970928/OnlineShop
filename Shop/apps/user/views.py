import random
import uuid

from django_redis import get_redis_connection
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import re
from user.helper import check_login, send_sms
from user.models import Users, Address
# Create your views here.
from django.views import View
from user.forms import RegisterModelForm, LoginModelForm, InforModelForm, AddressModelForm, PasswordModelForm, \
    ForgetModelForm
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


# 手机短信验证
class SendMsg(View):
    def get(self):
        pass

    def post(self, request):
        # 接收参数
        phone = request.POST.get('phone', '')
        rs = re.search('^1[3-9]\d{9}$', phone)
        # 判断参数的合法性
        if rs is None:
            return JsonResponse({'error': 1, 'errmsg': '电话号码格式不正确!'})
        # 生成随机验证码字符串
        random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        print('随机验证码为:{}'.format(random_code))

        # 保存验证码到redis中
        # 获取连接
        r = get_redis_connection()
        r.set(phone, random_code)
        # 设置60秒后过期
        r.expire(phone, 60)
        # 先获取当前手机号码的发送次数
        key_times = '{}_times'.format(phone)
        now_times = r.get(key_times)  # 是二进制内容,需要转换
        if now_times is None or int(now_times) < 5:
            # 保存手机号发送验证码的次数,不能超过5次
            r.incr(key_times)
            # 设置一个过期时间
            r.expire(key_times, 3600)  # 一个小时后再发送
        else:
            # 返回错误
            return JsonResponse({'error': 1, 'errmsg': '发送次数过多'})

        # # 连接运营商
        # __business_id = uuid.uuid1()
        # params = "{\"code\":\"%s\",\"product\":\"用户注册\"}" % random_code
        # # print(params)
        # rs = send_sms(__business_id, phone, "注册验证", "SMS_2245271", params)
        # print(rs.decode('utf-8'))
        # 合成响应
        return JsonResponse({'error': 0})


# 动态
@check_login
def message(request):
    return render(request, 'user/message.html')


# 发布动态
@check_login
def release(request):
    return render(request, 'user/release.html')


# 动态详情
@check_login
def messdetail(request):
    return render(request, 'user/messdetail.html')


# 我的详情
@check_login
def member(request):
    return render(request, 'user/member.html')


# 系统设置
@check_login
def step(request):
    return render(request, 'user/step.html')


# 个人资料
@check_login
def infor(request):
    id = request.session.get('ID')
    # 查询数据库
    data = Users.objects.filter(pk=id)
    # print(data)
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
        id = request.session.get('ID')
        # 接受参数
        data = request.POST
        user = Users.objects.get(pk=id)
        # 表单验证合法
        form = InforModelForm(data, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:个人资料')
        else:
            # 提示错误
            context = {
                'form': form
            }
            return render(request, 'user/addinfor.html', context=context)

# 关于我们
@check_login
def about(request):
    return render(request, 'user/about.html')


# 账户余额
@check_login
def records(request):
    return render(request, 'user/records.html')


# 积分
@check_login
def integral(request):
    return render(request, 'user/integral.html')


# 积分兑换
@check_login
def integralexchange(request):
    return render(request, 'user/integralexchange.html')


# 兑换记录
@check_login
def integralrecords(request):
    return render(request, 'user/integralrecords.html')


# 我的收藏
@check_login
def collect(request):
    return render(request, 'user/collect.html')


# 我的收藏编辑
@check_login
def collect_edit(request):
    return render(request, 'user/collect-edit.html')


# 收货地址
@check_login
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
@check_login
def saftystep(request):
    return render(request, 'user/saftystep.html')


# 修改密码
class PasswordView(View):
    def get(self, request):
        return render(request, 'user/password.html')

    def post(self, request):
        id = request.session.get('ID')
        # print(id)
        # 接受参数
        data = request.POST
        user = Users.objects.get(pk=id)
        # 表单验证合法
        form = PasswordModelForm(data, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:安全设置')
        else:
            # 提示错误
            context = {
                'form': form
            }
            return render(request, 'user/password.html', context=context)
# @check_login
# def password(request):
#     return render(request, 'user/password.html')


# 忘记密码
class ForgetView(View):
    def get(self, request):
        return render(request, 'user/forgetpassword.html')

    def post(self, request):
        # print(id)
        # 接受参数
        data = request.POST
        phone = data.get('phone')
        user = Users.objects.get(phone=phone)
        # 表单验证合法
        form = ForgetModelForm(data, instance=user)
        if form.is_valid():
            clened_data = form.cleaned_data
            user.password = set_password(clened_data.get('password'))
            user.save()
            return redirect('user:登录')
        else:
            # 提示错误
            context = {
                'form': form
            }
            return render(request, 'user/forgetpassword.html', context=context)
# def forgetpassword(request):
#     return render(request, 'user/forgetpassword.html')


# 支付密码
@check_login
def payment(request):
    return render(request, 'user/payment.html')


# 绑定手机
@check_login
def boundphone(request):
    return render(request, 'user/boundphone.html')


# 我的钱包
@check_login
def money(request):
    return render(request, 'user/money.html')


# 我要兼职
@check_login
def job(request):
    return render(request, 'user/job.html')


# 兼职申请记录
@check_login
def application(request):
    return render(request, 'user/application.html')


# 申请兼职
@check_login
def applicationjob(request):
    return render(request, 'user/applicationjob.html')


# 推荐有奖
@check_login
def recommend(request):
    return render(request, 'user/recommend.html')


# 我的推荐
@check_login
def myrecommend(request):
    return render(request, 'user/myrecommend.html')
