from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.shortcuts import *
from .models import *
from search.common import commonSearch
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm
from django.http.response import JsonResponse
from collect.models import Collection

class itemDetail(View):
    def post(self,request,pk):
        item = get_object_or_404(Item,pk = pk)
        form = CommentForm(request.POST)
        content_type = ContentType.objects.get_for_model(item)
        if form.is_valid():
            cmt = Comment()
            cmt.user = request.user
            cmt.text = form.cleaned_data['text']
            cmt.object_id = pk
            cmt.content_type = content_type
            cmt.save()
            # 保存评论
        return JsonResponse({})        

class itemList(View):
    def get(self,request):
        items = Item.objects.filter(sold = False)
        # 获取所有待售商品
        chopable = request.GET.get('chop',default = None)
        # 获取条件
        if chopable == '1':
            items = items.filter(chop = True)
            # 二次筛选
        sort = request.GET.get('sort',default = None)
        # 排序条件
        if sort:
            items = items.order_by(sort)

        search = request.GET.get('search',default = None)
        # 搜索关键词
        if search:
            items = commonSearch(Item,'name',search)
            # 调用自定义搜索函数
        
        type = ContentType.objects.get_for_model(Item())
        collections = Collection.objects.filter(user = request.user,content_type = type)
        # 筛选收藏 （通过object_id获取某用户收藏某商品的id）
        collect_ids = [c.object_id for c in collections]
        # id 集合
        for item in items:
            if item.id in collect_ids:
            # 打上标记
                item.is_collected = True
            else:
                item.is_collected = False
            item.save()
            content_type = ContentType.objects.get_for_model(item)
            # 对象的类
            comments = Comment.objects.filter(content_type = content_type,object_id = item.pk)
            # 获取评论
            item.comments = comments
            # 添加属性
        context = {
            'items' : items,
            'chop' : chopable,
            'sort' : sort,
        }
        return render(request,'itemList.html',context)