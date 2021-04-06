from django.shortcuts import *
from django.views.generic import *

class ChatRoom(View):
    def get(self,request):
        response = render(request,'chatroom.html',{
        })
        return response