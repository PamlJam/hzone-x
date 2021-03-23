from blog.models import Atc
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .forms import *

class ReleaseArticle(View):
    def get(self,request):
        return render(request,'releaseArticle.html',{
            'form' : ArticleForm(request.GET),
        })
    def post(self,request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            tt = form.cleaned_data['tt']
            ct = form.cleaned_data['ct']
            tp = form.cleaned_data['tp']
            # 获取分类编号
            tp = AtcType.objects.all()[int(tp)]
            # 获取分类对象
            Atc(title= tt,content= ct,type = tp,author = request.user).save()
            # 生成文章对象
        return JsonResponse({})

class Release(View):
    def get(self,request):
        return render(request,'release.html',{})

    def post(self,request):
        return render(request,'release.html',{})