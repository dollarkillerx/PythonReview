# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 21:16 
# @Author : DollarKillerx
# @Description : pickle

import pickle

# 定义存储文件名称
shoplistfile = 'pickle.data'


def f1():
    data = input("you data:")
    f = open(shoplistfile, 'wb')  # 写
    # write
    pickle.dump(data, f)
    f.close()


def f2():
    f = open(shoplistfile, 'rb')  # 读
    storedlist = pickle.load(f)
    print(storedlist)
    f.close()


if __name__ == '__main__':
    f1()
    f2()
