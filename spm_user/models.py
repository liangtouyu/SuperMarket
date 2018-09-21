from django.core import validators
from django.db import models

# Create your models here.


class Register(models.Model):
    phone = models.SmallIntegerField(verbose_name='手机号')
    pwd = models.CharField(max_length=50,
                           validators=[validators.MinLengthValidator(6)],
                           verbose_name='密码')
    identifying_code = models.CharField(max_length=20,verbose_name='验证码')

    is_delete = models.BooleanField(default=False,verbose_name='是否删除')

