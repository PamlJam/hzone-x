from blog.models import Atc
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .forms import *
from markdown import markdown
from tomd import Tomd

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
# 编辑文章
    def get(self,request):
        pk = request.GET.get('pk',default = None)
        context = {}
        if pk:
            atc = get_object_or_404(Atc,pk = int(pk))
            if atc.author == request.user:
                context['ex_tt'] = atc.title
                context['ex_ct'] = Tomd(atc.content).markdown
        request.session['atc_pk'] = atc.pk
        request.session['ex_atc'] = context
        # 存入原始数据
        return redirect('/release')

class ReleaseArticle(View):
# 发布文章
    def get(self,request):
        context = request.session.get('ex_atc',default = {})
        # 取出原始数据（设置默认值）
        if context == {}:
        # 取值失败
            request.session['atc_pk'] = None
            # 总是清空 **
        context['form'] = ArticleForm(request.GET)
        # 渲染表单
        request.session['ex_atc'] = {}
        # 清空原始值（防止重复使用）
        return render(request,'releaseArticle.html',context)

    def post(self,request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            tt = form.cleaned_data['tt']
            ct = form.cleaned_data['ct']
            # 文章内容
            ct = markdown(
            # 转换格式
                ct,
                # 传入内容
                extensions=[
                # 拓展
                    'markdown.extensions.extra',
                    # 常用设置
                    'markdown.extensions.toc',
                    # 文章目录
                ]
            )
            tp = form.cleaned_data['tp']
            # 获取分类编号
            tp = AtcType.objects.all()[int(tp)]
            # 获取分类对象
            pk = request.session.get('atc_pk',default = None)
            # 会话取值
            if pk != None and 1:
            # 判断请求来源
                exAtc = get_object_or_404(Atc,pk = pk)
                exAtc.title = tt
                exAtc.content = ct
                exAtc.type = tp
                exAtc.author = request.user
                exAtc.save()
                request.session['atc_pk'] = None
                # 总是清空 **
            else:
                Atc(title= tt,content= ct,type = tp,author = request.user).save()
                # 生成文章对象
        return JsonResponse({})

class Release(View):
    def get(self,request):
        return render(request,'release.html',{})