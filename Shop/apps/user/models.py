from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.

class Users(models.Model):
    gender_choices = (
        (1, '男'),
        (2, '女'),
        (3, '保密'),
    )
    phone = models.CharField(max_length=11,
                             validators=[
                                 MinLengthValidator(11, '手机号长度不正确'),
                                 RegexValidator(r'^1[3-9]\d{9}$', '手机号码格式不正确')
                             ], verbose_name='手机号码')
    user_name = models.CharField(max_length=16,
                                 validators=[
                                     MinLengthValidator(4, '昵称最少有4个字符')
                                 ], null=True, verbose_name='昵称'
                                 )
    password = models.CharField(max_length=32, verbose_name='密码')
    gender = models.SmallIntegerField(choices=gender_choices, default=3, verbose_name='性别')
    birthday = models.DateField(null=True, verbose_name='生日')
    school = models.CharField(max_length=100, null=True, verbose_name='学校')
    address = models.CharField(max_length=200, null=True, verbose_name='详细地址')
    hometown = models.CharField(max_length=100, null=True, verbose_name='老家')

    is_delete = models.BooleanField(default=False, verbose_name='删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')  # 修改时间

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'users'
