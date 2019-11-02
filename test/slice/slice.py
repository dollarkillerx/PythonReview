# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 17:32 
# @Author : DollarKillerx
# @Description :

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = a[2:]
    b[0] = 1223
    print(b)
    print(a)
    # Python的切片和Golang还是有一点区别的
    # for i,b in range(a):
    #     print(i,b)
    print(len(a))
    for i in range(len(a)):
        print(a[i])