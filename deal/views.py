from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.shortcuts import *
from .models import *

class itemList(View):
    def get(self,request):
        items = Item.objects.all()
        context = {
            'items' : items,
        }
        return render(request,'itemList.html',context)