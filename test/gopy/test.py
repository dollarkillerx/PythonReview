# -*- coding: utf-8 -*- 
# @Time : 2019-10-31 21:05 
# @Author : DollarKillerx
# @Description :

import ctypes

if __name__ == '__main__':
    add = ctypes.CDLL('./libadd.so').add
    # 显式声明参数和返回的期望类型
    add.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    add.restype = ctypes.c_char_p
    left = "Hello".encode("utf-8")
    right = "World".encode("utf-8")
    resp = add(left, right)
    resp = resp.decode("utf-8")
    print(resp)