from deal.views import *
from django.urls import path

urlpatterns = [
    path('',itemList.as_view()),
]