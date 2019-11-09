from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests
from get_by_douban import def_response
# Create your views here.

class Music(View):
    DOUBAN_MUSIC_API = 'https://api.douban.com/v2/music/search?q={}'
    def get(self,request):
        music_name = request.GET.get('musicname','')
        if not music_name:
            return JsonResponse({'errcode':-1,'errmsg':'音乐名称不能为空'})
        url = Music.DOUBAN_MUSIC_API.format(music_name)
        response = requests.get(url)
        data = response.json()
        return JsonResponse({'errcode':0,'errmsg':data})

class Book(View):
    DOUBAN_BOOK_API = 'https://douban.uieee.com/v2/book/search?q={}'
    def get(self,request):
        bookname = request.GET.get('bookname','')
        if not bookname:
            return def_response.respErr400()
        url = Book.DOUBAN_BOOK_API.format(bookname)
        try:
            response = requests.get(url)
        except Exception as e:
            return def_response.respErr500({"msg":str(e)})
        data = response.json()
        return def_response.responseJson(200,{'data':data})
