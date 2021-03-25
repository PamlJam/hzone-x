from blog.models import Atc
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .forms import *
import markdown
from tomd import Tomd
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
                if Tomd(atc.content).markdown:
                # 若原始内容包含html内容格式
                    atc.content = Tomd(atc.content).markdown
                    # 二次反转格式 -> markdown
                context['ex_ct'] = atc.content
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
        md = markdown.Markdown(
        # 语法转换器
            extensions = [
            # 拓展语法
                'markdown.extensions.extra',
                # 常用设置
                'markdown.extensions.toc',
                # 添加标签
            ]
        )
        form = ArticleForm(request.POST)
        if form.is_valid():
            tt = form.cleaned_data['tt']
            ct = form.cleaned_data['ct']
            # 文章内容
            ct = md.convert(ct)
            ct = Tomd(ct).markdown
            ct = md.convert(ct)
            # 反复的格式转换 **** 
            # md、html语法混合 —> markdown —> html
            toc = md.toc
            # 获取目录 —> html
            tp = form.cleaned_data['tp']
            # 获取分类编号
            tp = AtcType.objects.all()[int(tp)]
            # 获取分类对象
            pk = request.session.get('atc_pk',default = None)
            # 会话取值
            if pk != None:
            # 判断请求来源
                exAtc = get_object_or_404(Atc,pk = pk)
                exAtc.title = tt
                exAtc.content = ct
                exAtc.type = tp
                exAtc.toc = toc
                exAtc.author = request.user
                exAtc.save()
                request.session['atc_pk'] = None
                # 总是清空 **
            else:
                Atc(title= tt,content= ct,type = tp,toc = toc,author = request.user).save()
                # 生成文章对象
        return JsonResponse({})

class Release(View):
    def get(self,request):
        return render(request,'release.html',{})