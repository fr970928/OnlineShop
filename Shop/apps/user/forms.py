from django import forms

from user import set_password
from user.models import Users, Address


# 注册界面的Form


class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不能少于6个字符',
                                   'max_length': '密码不能超过16个字符'
                               })
    re_password = forms.CharField(max_length=16,
                                  min_length=6,
                                  error_messages={
                                      'required': '重复密码不能为空',
                                      'min_length': '密码不能少于6个字符',
                                      'max_length': '密码不能超过16个字符',
                                  })

    class Meta:
        model = Users
        fields = ['phone']
        error_messages = {
            'phone': {
                'required': '手机号不能为空',
                'max_length': '手机号长度不正确',
            }
        }

    # 验证手机号是否存在
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        res = Users.objects.filter(phone=phone).exists()
        # 用户名存在时
        if res:
            raise forms.ValidationError('该手机号已经存在')
        else:
            return phone

    # 判断两次密码是否一致
    def clean(self):
        pas = self.cleaned_data.get('password')
        re_pas = self.cleaned_data.get('re_password')
        if pas and re_pas and pas != re_pas:
            raise forms.ValidationError({'re_password': '两次密码不一致'})

            # 验证 用户传入的验证码和redis中的是否一样
            # 用户传入的
            try:
                captcha = self.cleaned_data.get('captcha')
                phone = self.cleaned_data.get('phone', '')
                # 获取redis中的
                r = get_redis_connection()
                random_code = r.get(phone)  # 二进制, 转码
                random_code = random_code.decode('utf-8')
                # 比对
                if captcha and captcha != random_code:
                    raise forms.ValidationError({"captcha": "验证码输入错误!"})
            except:
                raise forms.ValidationError({"captcha": "验证码输入错误!"})
        return self.cleaned_data


# 判断登录界面的Form
class LoginModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不能少于6个字符',
                                   'max_length': '密码不能超过16个字符',
                               })

    class Meta:
        model = Users
        fields = ['phone']
        error_messages = {
            'phone': {
                'required': '手机号不能为空',
                'max_length': '手机号长度不正确',
            }
        }

    def clean(self):
        # 验证用户名
        # 查询数据库
        phone = self.cleaned_data.get('phone')
        try:
            user = Users.objects.get(phone=phone)
        except Users.DoesNotExist:
            raise forms.ValidationError({'phone': '手机号错误'})

        # 验证密码
        password = self.cleaned_data.get('password', '')
        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误'})

        self.cleaned_data['user'] = user
        return self.cleaned_data


# 判断修改个人资料
class InforModelForm(forms.ModelForm):
    user_name = forms.CharField(max_length=16,
                                min_length=4,
                                error_messages={
                                    'required': '昵称不能为空',
                                    'min_length': '昵称长度不能低于4个字符',
                                    'max_length': '昵称长度不能低于16个字符'}
                                )

    class Meta:
        model = Users
        exclude = ['phone', 'password']


# 判断修改密码
class PasswordModelForm(forms.ModelForm):
    id = forms.CharField()
    new_password = forms.CharField(max_length=16,
                                   min_length=6,
                                   error_messages={
                                       'required': '密码不能为空',
                                       'min_length': '密码不能少于6个字符',
                                       'max_length': '密码不能超过16个字符'
                                   })
    re_new_password = forms.CharField(max_length=16,
                                      min_length=6,
                                      error_messages={
                                          'required': '重复密码不能为空',
                                          'min_length': '密码不能少于6个字符',
                                          'max_length': '密码不能超过16个字符',
                                      })

    class Meta:
        model = Users
        fields = ['password', 'id']

    def clean(self):
        id = self.cleaned_data.get('id')
        password = self.cleaned_data.get('password', '')
        res = Users.objects.get(pk=id)
        if res.password != set_password(password):
            raise forms.ValidationError({'password': '密码不正确'})
        # 判断两次新密码是否一致
        new_pas = self.cleaned_data.get('new_password')
        re_new_pas = self.cleaned_data.get('re_new_password')
        if new_pas and re_new_pas and new_pas != re_new_pas:
            raise forms.ValidationError({'re_new_password': '两次密码不一致'})
        return self.cleaned_data


# 判断忘记密码
class ForgetModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不能少于6个字符',
                                   'max_length': '密码不能超过16个字符'
                               })
    re_password = forms.CharField(max_length=16,
                                  min_length=6,
                                  error_messages={
                                      'required': '重复密码不能为空',
                                      'min_length': '密码不能少于6个字符',
                                      'max_length': '密码不能超过16个字符',
                                  })

    class Meta:
        model = Users
        fields = []

    def clean(self):
        pas = self.cleaned_data.get('password')
        re_pas = self.cleaned_data.get('re_password')
        if pas and re_pas and pas != re_pas:
            raise forms.ValidationError({'re_password': '两次密码不一致'})

            # 验证 用户传入的验证码和redis中的是否一样
            # 用户传入的
            try:
                captcha = self.cleaned_data.get('captcha')
                phone = self.cleaned_data.get('phone', '')
                # 获取redis中的
                r = get_redis_connection()
                random_code = r.get(phone)  # 二进制, 转码
                random_code = random_code.decode('utf-8')
                # 比对
                if captcha and captcha != random_code:
                    raise forms.ValidationError({"captcha": "验证码输入错误!"})
            except:
                raise forms.ValidationError({"captcha": "验证码输入错误!"})
        return self.cleaned_data


# 判断收货地址
class AddressModelForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           error_messages={
                               'required': '收货人不能为空'
                           })
    telephone = forms.CharField(max_length=11,
                                min_length=11,
                                error_messages={
                                    'required': '电话不能为空',
                                    'min_length': '电话长度不正确',
                                    'max_length': '电话长度不正确'
                                })
    province = forms.CharField(max_length=50,
                               error_messages={
                                   'required': '省份不能为空'
                               })
    city = forms.CharField(max_length=50,
                           error_messages={
                               'required': '城市不能为空'
                           })
    area = forms.CharField(max_length=50,
                           error_messages={
                               'required': '地区不能为空'
                           })
    brief = forms.CharField(max_length=50,
                            error_messages={
                                'required': '详细地址不能为空'
                            })

    class Meta:
        model = Address
        exclude = ['']
