from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import *
from .models import *
from deal.models import Item

class Change(View):
    def get(self,request,pk):
        user = request.user
        item = get_object_or_404(Item,pk = pk)
        content_type = ContentType.objects.get_for_model(item)
        collections = Collection.objects.filter(
            user = user,
            content_type = content_type,
            object_id = pk,
        )
        if collections:
            collections.delete()
            # 删除关系
            item.is_collected = False
        else:
            Collection(
                user = user,
                content_type = content_type,
                object_id = pk,
            ).save()
            item.is_collected = True
        return redirect('/deal')