# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 22:19 
# @Author : DollarKillerx
# @Description : 函数式编程

def test1():
    return lambda x, y: x + y


def test2(x, y):
    return x if x > y else y


if __name__ == '__main__':
    print(test1()(1, 2))
    print(test2(1, 2))
