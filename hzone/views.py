from django.shortcuts import *
# 快捷函数
from django.views.generic import *
# 通用视图
# from crawler import school

class Index(View):
# 类视图
    def get(self,request):
    # 请求方式
        response = render(request,'index.html',{
            'infos' : {},# school.get_infos()
            # 爬取信息（暂不使用，防止卡死）
        })
        return response

class About(View):
    def get(self,request):
        return render(request,'about.html',{})