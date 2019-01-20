from django import forms

from user import set_password
from user.models import Users

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
        else:
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
