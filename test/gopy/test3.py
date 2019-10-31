# -*- coding: utf-8 -*- 
# @Time : 2019-10-31 21:28 
# @Author : DollarKillerx
# @Description :

from ctypes import cdll

if __name__ == '__main__':
    test = cdll.LoadLibrary("./libtest.so")
    resp1 = test.Set(12)
    print(resp1)
    resp2 = test.Get()
    print(resp2)