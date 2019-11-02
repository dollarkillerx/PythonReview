# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 21:06 
# @Author : DollarKillerx
# @Description : 文件操作

def test1():
    inp = input("输入ppc:")
    f = open('cos.txt', 'w')
    f.write(inp)
    f.close()


def test2():
    f = open('cos.txt', 'r')
    a = f.read()  # 读全部
    print(a)


def test3():
    f = open('cos.txt','r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end=' ')


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
