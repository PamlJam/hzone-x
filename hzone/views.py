from django.shortcuts import *
# 快捷函数
from django.views.generic import *
# 通用视图
from crawler import schoolInfo

class Index(View):
# 类视图
    def get(self,request):
    # 请求方式
        response = render(request,'index.html',{
            'infos' : schoolInfo.getInfos(),
            # 爬虫取值
        })
        return response