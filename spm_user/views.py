from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from spm_user.form import RegModelForm
from spm_user.models import Register


def member(request):
    return render(request, 'spm_user/member.html')


def login(request):
    return render(request, 'spm_user/login.html')


def register(request):
    # 1.接收参数
    # request.POST     全部获取
    # request.POST.get(字段名)  获取单个
    if request.method == "POST":
        data = request.POST
        # phone = data.get('phone')
        # pwd = data.get('pwd')
        # identifying_code = data.get('identifying_code')
        form = RegModelForm(data)
        # 2.处理数据
        # Register.objects.create(phone=phone,pwd=pwd,identifying_code=identifying_code)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        else:
            # 显示错误信息
            return render(request, 'spm_user/reg.html')

    # 3.响应
    else:
        # return HttpResponse('ok')
        return render(request, 'spm_user/reg.html')
