# -*- coding: utf-8 -*- 
# @Time : 2019-11-03 16:04 
# @Author : DollarKillerx
# @Description : urls

from django.urls import path
from .views import hello,ppc,Test

urlpatterns = [
    path('', hello),
    path('he/<str:name>/<int:age>',ppc),
    path('test/',Test.as_view())
]
