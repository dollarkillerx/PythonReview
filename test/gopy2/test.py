# -*- coding: utf-8 -*- 
# @Time : 2019-10-31 21:49 
# @Author : DollarKillerx
# @Description :

# from ctypes import cdll, c_char_p
import ctypes

if __name__ == '__main__':
    # libhttp = cdll.LoadLibrary("./libhttp.so")
    # libhttp.Get.argtypes = [c_char_p]
    # libhttp.Get.restype = c_char_p
    #
    # url = "https://www.baidu.com".encode("utf-8")
    # resp = libhttp.Get(url)
    # resp = resp.decode("utf-8")
    #
    # print(resp)
    get = ctypes.CDLL('./libhttp.so').Get
    # 显式声明参数和返回的期望类型
    get.argtypes = [ctypes.c_char_p]
    get.restype = ctypes.c_char_p
    left = "Hello".encode("utf-8")
    resp = get(left)
    resp = resp.decode("utf-8")
    print(resp)
