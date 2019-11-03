# coding:utf-8
from django.http import HttpResponse
from django.views.generic import View


def hello(request):
    name = request.GET.get('name', '')
    return HttpResponse("hello django {}".format(name))


def ppc(request, name, age):
    # print(dir(request))
    return HttpResponse("you name:{}  age:{}".format(name, age))


class Test(View):
    def get(self, request):
        return HttpResponse("this is test class")
