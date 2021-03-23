from django.core import paginator
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .models import *
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm
from search.forms import SearchForm
from search.common import commonSearch
from django.db.models.aggregates import Count
from django.core.paginator import Paginator

class SearchList(View):
    def get(self,request):
        context = {}
        form = SearchForm(request.GET)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            context['atcs'] = commonSearch(Atc,'title',keywords)
        return render(request,'searchlist.html',context)

class List(View):
    def get(self,request):
        data = request.GET.get('type',default = None)
        # 获取携带参数
        if data:
            type = get_object_or_404(AtcType,name = data)
            atcs = Atc.objects.filter(type = type)
        else:
            atcs = Atc.objects.all()
        p = Paginator(atcs,5)
        # 设置分页
        n = request.GET.get("p",default = 1)
        
        context = {
            'form' : SearchForm(request.GET),
            'atcs' : p.get_page(n),
            # 获取分页
            'types' : AtcType.objects.annotate(num = Count('atc')),
            # 获取所有分类 + 统计分类数目
        }
        return render(request,'list.html',context)

class Detail(View):
    def ret(self,request,pk):
    # 获取字典
        article = get_object_or_404(Atc,pk = pk)
        content_type = ContentType.objects.get_for_model(article)
        # 对象的类
        comments = Comment.objects.filter(content_type = content_type,object_id = article.pk)
        # 获取评论
        context = {
            'atc' : article,
            'cms' : comments,
            'type' : content_type,
        }
        return context

    def get(self,request,pk):
        context = self.ret(request,pk)
        context['form'] = CommentForm(request.GET)
        # 生成空表
        return render(request,'detail.html',context)

    def post(self,request,pk):
        form = CommentForm(request.POST)
        # 填写表单
        if form.is_valid():
        # 验证数据
            cmt = Comment()
            # 新建评论
            cmt.user = request.user
            # 当前用户
            cmt.text = form.cleaned_data['text']
            # 字典取值
            context = self.ret(request,pk)
            cmt.object_id = pk
            cmt.content_type = context['type']
            cmt.save()
            # 保存评论
        return JsonResponse({})