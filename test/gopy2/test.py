# -*- coding: utf-8 -*- 
# @Time : 2019-10-31 21:49 
# @Author : DollarKillerx
# @Description :

from ctypes import cdll, c_char_p

if __name__ == '__main__':
    libconcat = cdll.LoadLibrary("./libhttp.so")
    libconcat.Concat.argtypes = [c_char_p]
    libconcat.Concat.restype = c_char_p

    url = "https://www.baidu.com".encode("utf-8")
    resp = libconcat.Get(url)
    resp = resp.decode("utf-8")

    print(resp)
