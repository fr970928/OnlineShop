from django.core.validators import MinLengthValidator
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
                                 MinLengthValidator(11, '手机号只有11个字符')
                             ])
    user_name = models.CharField(max_length=16,
                                 validators=[
                                     MinLengthValidator(4, '昵称最少有4个字符')
                                 ], null=True
                                 )
    password = models.CharField(max_length=32)
    gender = models.SmallIntegerField(choices=gender_choices, default=3)
    school = models.CharField(max_length=100, null=True)
    hometown = models.CharField(max_length=100, null=True)

    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)  # 修改时间

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'users'
