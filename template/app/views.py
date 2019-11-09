# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Index(View):
    # TEMPLATE = 'index.html'
    TEMPLATE = 'index3.html'
    def get(self,request,name):
        data = {}
        data['name'] = name
        data['array'] = range(10)
        return render(request,Index.TEMPLATE,data)
