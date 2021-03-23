from blog.models import Atc
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .forms import *


class ArticleDelete(View):
# 删除内容
    def get(self,request):
        pk = request.GET.get('pk',default = None)
        if pk:
            atc = get_object_or_404(Atc,pk = int(pk))
            # 获取文章
            if atc.author == request.user:
            # 验证权限
                atc.delete()
                # 删除模型 （实际删除）
        return redirect('/user/' + str(request.user.id))

class ArticleEdit(View):
    def get(self,request):
        pass

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