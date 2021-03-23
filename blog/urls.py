from blog.views import *
from django.urls import path

urlpatterns = [
    path('result',SearchList.as_view()),
    path('',List.as_view()),
    path('<int:pk>',Detail.as_view()),
]