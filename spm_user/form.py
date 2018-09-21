from django import  forms

from spm_user.models import Register


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Register
        fields =['phone','pwd','identifying_code','is_delete']
        error_messages ={
            'phone':{
                'required': '电话号码必须填写',
            },
            'pwd': {
                'required': '密码必须填写',
                'max_length': '密码不能大于50位',
                'min_length': '密码不能小于6位'
            }
        }

