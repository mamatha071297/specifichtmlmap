from django.urls import path
from app1.views import *

app_name='app1'

urlpatterns=[
    path('mamatha/',mamatha,name='mamatha'),
]