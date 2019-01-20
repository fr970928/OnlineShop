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
        fields = ['user_name']
        error_messages = {
            'user_name': {
                'required': '用户名不能为空',
                'max_length': '用户名不能超过20个字符',
            }
        }

    # 验证用户名是否存在
    def clean_user_name(self):
        # 查询数据库
        uesr_name = self.cleaned_data.get('user_name')
        res = Users.objects.filter(user_name=uesr_name).exists()
        # 用户名存在时
        if res:
            raise forms.ValidationError('该用户名已经存在')
        else:
            return uesr_name

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
        fields = ['user_name']
        error_messages = {
            'user_name': {
                'required': '用户名不能为空',
                'max_length': '用户名不能超过20个字符',
            }
        }

    def clean(self):
        # 验证用户名
        # 查询数据库
        user_name = self.cleaned_data.get('user_name')
        try:
            user = Users.objects.get(user_name=user_name)
        except Users.DoesNotExist:
            raise forms.ValidationError({'user_name': '用户名错误'})

        # 验证密码
        password = self.cleaned_data.get('password', '')
        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误'})

        self.cleaned_data['user'] = user
        return self.cleaned_data
