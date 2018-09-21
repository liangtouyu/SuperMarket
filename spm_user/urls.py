from django.conf.urls import url

from spm_user.views import member, register, login

urlpatterns = [
    url(r'^member/$', member, name='个人中心'),
    url(r'^reg/$', register, name='注册'),
    url(r'^login/$', login, name='登录'),
]
