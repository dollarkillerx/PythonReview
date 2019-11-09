from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests
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