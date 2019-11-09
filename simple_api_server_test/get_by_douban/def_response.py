# coding:utf-8
# 定义response 通用对象模型
from django.http import JsonResponse

def responseJson(code:int,data):
    """
    返回包装JsonResponse
    code: httpCode
    data: respBody
    """
    resp = JsonResponse(data)
    resp.status_code = code
    return resp

def respErr400():
    """
    包装返回400 
    """
    return responseJson(400,Err400)

def respErr500(data):
    """
    返回用户500的错误信息
    """
    return responseJson(500,data)

# 定义相关默认返回对象
Err400 = {"code":400,"msg":"用户输入参数错误"}