from django.contrib import admin
from django.urls import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('chat/',include('chat.urls')),
    path('user/',include('user.urls')),
    path('blog/',include('blog.urls')),
    path('deal/',include('deal.urls')),
    path('collect/',include('collect.urls')),
    path('release/',include('release.urls')),
]
