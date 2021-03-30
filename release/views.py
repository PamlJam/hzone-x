from blog.models import Atc
from django.http.response import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from .forms import *
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from deal.models import Item

class ItemEdit(View):
    def get(self,request):
        pk = request.GET.get('pk',default = None)
        context = {}
        if pk:
            item = get_object_or_404(Item,pk = int(pk))
            if item.owner == request.user:
                context['itemId'] = item.pk
                context['itemName'] = item.name
                context['itemInfo'] = item.info
                context['itemPrice'] = item.price
                context['itemCount'] = item.count
                context['itemImage'] = str(item.image)
                print(str(item.image))
                # 必须传入Json格式
        request.session['itemPk'] = item.pk
        request.session['context'] = context
        return redirect('/release')

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

class ItemDelete(View):
    def get(self,request):
        pk = request.GET.get('pk',default = None)
        user = request.user
        if pk:
            item = get_object_or_404(Item,pk = int(pk))
            if item.owner == user:
                content_type = ContentType.objects.get_for_model(item)
                comments = Comment.objects.filter(content_type = content_type,object_id = item.pk)
                comments.delete()
                item.delete()
        return redirect('/user/' + str(user.id))

class ReleaseItem(View):
# 发布文章
    def get(self,request):
        form = ItemForm()
        context = request.session.get('context',default = {})
        if context == {}:
            request.session['itemPk'] = None
        request.session['context'] = {}
        return render(request,'releaseItem.html',context)

    def post(self,request):
        context = {}
        form = ItemForm(request.POST,request.FILES)
        # 完全填写表格
        if form.is_valid():
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']
            info = form.cleaned_data['info']
            sold = form.cleaned_data['sold']
            chop = form.cleaned_data['chop']
            count = form.cleaned_data['count']
            price = form.cleaned_data['price']
            pk = request.session.get('itemPk',default = None)
            if pk != None:
                exItem = get_object_or_404(Item,pk = pk)
                exItem.chop = chop
                exItem.sold = sold
                exItem.name = name
                exItem.info = info                
                exItem.count = count                
                exItem.price = price
                exItem.save()
                request.session['itemPk'] = None
            else:
                item = Item(
                    name = name,
                    info = info,
                    sold = sold,
                    chop = chop,
                    image = image,
                    count = int(count),
                    price = float(price),
                    owner = request.user,
                )
                if image:
                    item.image = image
                # 避免自动生成的乱码                    
                item.save()
            context['status'] = "SUCCESS"
        else:
            context['status'] = "ERROR"
        return JsonResponse(context)
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
        context = {}
        if request.session.get('itemPk',default = None):
            context['isItem'] = 1
        else:
            context['isItem'] = 0
        return render(request,'release.html',context)

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