from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=20,
                                 validators=[
                                     MinLengthValidator(6, '用户名至少有6个字符')
                                 ])
    password = models.CharField(max_length=32)

    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'users'
