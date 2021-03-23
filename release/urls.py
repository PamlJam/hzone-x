from django.urls import path
from .views import *

urlpatterns = [
    path('',Release.as_view()),
    path('article',ReleaseArticle.as_view()),
]