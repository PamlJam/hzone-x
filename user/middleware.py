from django.http import *
from django.shortcuts import redirect

class MyMiddleWare:
# 基于类
    def __init__(self,get_response):
    # 初始执行
        self.get_response = get_response

    def __call__(self,request):
    # 调用执行
        if request.user.is_authenticated == False:
        # 用户状态
            if 'sign' not in request.path:
            # 路径包含 (谨防无限递归)
                return redirect('/user/sign-in')
                # 引发短路
        else:
        # 两个状态不可能同时存在
            if 'sign' in request.path:
                return redirect('/')
        response = self.get_response(request)
        # 执行视图
        return response