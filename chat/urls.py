from django.urls import path
from .views import *

urlpatterns = [
    path('', ChatRoom.as_view()),
]