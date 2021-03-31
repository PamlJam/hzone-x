from collect.views import Change
from blog.views import *
from django.urls import path

urlpatterns = [
    path('<int:pk>',Change.as_view()),
]