from blog.models import Atc
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .forms import *
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment

class ArticleDelete(View):
# 删除内容
    def get(self,request):
        pk = request.GET.get('pk',default = None)
        if pk:
            atc = get_object_or_404(Atc,pk = int(pk))
            # 获取文章
            if atc.author == request.user:
            # 验证权限
                content_type = ContentType.objects.get_for_model(atc)
                comments = Comment.objects.filter(content_type = content_type,object_id = atc.pk)
                comments.delete()
                # 删除所有互动（评论）
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
                # 获取已有标题
                context['ex_ct'] = atc.content
                # 获取原有文章
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
            tp = form.cleaned_data['tp']
            # 分类编号
            tp = AtcType.objects.all()[int(tp)]
            # 分类对象
            pk = request.session.get('atc_pk',default = None)
            # 会话取值
            if pk != None:
            # 请求来源
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
                # 文章对象
        return JsonResponse({})

class Release(View):
    def get(self,request):
        return render(request,'release.html',{})