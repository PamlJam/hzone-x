from django.urls import path
from .views import *

urlpatterns =[
    path('<int:pk>',Room.as_view()),
    path('sign-up',SignUp.as_view()),
    path('sign-in',SignIn.as_view()),
    path('sign-info',SignInfo.as_view()),
    path('exit',Exit.as_view()),
]