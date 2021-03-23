from django.http.response import JsonResponse
from django.shortcuts import *
# 快捷函数
from django.views.generic import *
# 通用视图
from .models import *
from .forms import *
from blog.models import Atc
from django.contrib.auth import *

class Room(View):
# 个人空间
    def get(self,request,pk):
	# 接收参数
        form = userForm()
        # 空表
        user = get_object_or_404(User,pk = pk)
        # 请求对象
        context = {
            'visitor' :request.user,
            # 访客
            'user' : user,
            # 主人
            'form' : form,
            'atcs' : Atc.objects.filter(author = user),
        }
        return render(request,'room.html',context)
        
    def post(self,request,pk):        
        user= request.user
        form = userForm(request.POST,request.FILES)
        # 填写
        if form.is_valid():
        # 验证
            icon,motto = [value for value in form.cleaned_data.values()]
            # 遍历赋值
            if icon:
            # 有效改动
                user.icon = icon
            if motto:
                user.motto = motto       
            user.save()
            # 更新资料
        return redirect('/user/' + str(user.id))
        # 重定向

class SignInfo(View):
    def get(self,request):
        return render(request,'sign-info.html',{})
        
class SignUp(View):
    def get(self,request):
        return render(request,'sign-up.html',{
            'form' : SignForm(request.GET),
        })

    def post(self,request):        
        form = SignForm(request.POST)
        context = {}
        if form.is_valid():
            un = form.cleaned_data['un']
            pw = form.cleaned_data['pw']
            re = form.cleaned_data['re']
            if not(5<=len(un) <=9 or 5<=len(pw)<=9):
            # 长度规范
                context['status'] = 'leng'
            elif User.objects.filter(username = un):
            # 命名重复
                context['status'] = 'same'
            elif pw != re:
            # 输入一致
                context['status'] = 'diff'
            else:
                newone = User.objects.create_user(un,None,pw)
                # 生成用户
                newone.save()
                # 保存用户
                login(request, newone)
                # 自动登录
                context['status'] = 'succ'
        return JsonResponse(context)

class SignIn(View):
    def get(self,request):
        return render(request,'sign-in.html',{
            'form' : SignForm(request.GET),
        })
    def post(self,request):
        form = SignForm(request.POST)
        context = {}
        if form.is_valid():
            un = form.cleaned_data['un']
            pw = form.cleaned_data['pw']
            user = authenticate(request, username=un, password=pw)
            # 验证用户
            if user is not None: 
                login(request, user)
                # 用户登录
                context['status'] = 'succ'
            else:
                context['status'] = 'erro'
        return JsonResponse(context)


class Exit(View):
# 用户登出
    def get(self,request):
        if request.user.is_authenticated:
        # 验证状态
            logout(request)
        return redirect('/')