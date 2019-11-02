# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 17:39 
# @Author : DollarKillerx
# @Description :

def hello(a, v=12):
    print(a, v)


def he(*args):
    for i in args:
        print(i)
    # print(args)


def hhe(a, b):
    global cs
    cs = 23333
    return a, b


def maps():
    '''
    这个是文档字符串 哈哈哈
    map 遍历的test
    :return:
    '''
    cs = {"a": 23, "b": 23, "d": 343}
    for i, v in cs.items():
        print(i, v)
    for _, v in cs.items():
        print(v)


if __name__ == '__main__':
    # hello(1)
    # hello(2, 34)
    # he(1, 2, 343)
    # _, b = hhe(1, 2)  # 爽歪歪可以和golang一样玩耍
    # print(b)
    # print(cs)
    maps()
    print(maps.__doc__)
