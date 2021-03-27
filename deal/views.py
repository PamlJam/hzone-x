from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.shortcuts import *
from .models import *

class itemList(View):
    def get(self,request):
        items = Item.objects.all()
        chopable = request.GET.get('chop',default = None)
        # 获取条件
        if chopable == '1':
            items = items.filter(chop = True)
            # 二次筛选
        sort = request.GET.get('sort',default = None)
        # 排序条件
        if sort:
            items = items.order_by(sort)
        context = {
            'items' : items,
            'chop' : chopable,
            'sort' : sort,
        }
        return render(request,'itemList.html',context)