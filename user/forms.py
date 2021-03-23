from django import forms
from .models import *

class SignForm(forms.Form):
# 用于注册&登录
    un = forms.CharField(required=True)
    pw = forms.CharField(widget=forms.PasswordInput,required=True)
    re = forms.CharField(widget=forms.PasswordInput,required=False)

class userForm(forms.Form):
# 用于更新用户资料
    icon = forms.ImageField(label = '用户头像',required= False)
    # 非必须字段
    motto = forms.CharField(label= '个性签名',required= False)