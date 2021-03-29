from django.urls import path
from .views import *

urlpatterns = [
    path('',Release.as_view()),

    path('article',ReleaseArticle.as_view()),
    path('article/edit',ArticleEdit.as_view()),
    path('article/delete',ArticleDelete.as_view()),

    path('item',ReleaseItem.as_view()),
    path('item/delete',ItemDelete.as_view()),
    path('item/edit',ItemEdit.as_view()),
]