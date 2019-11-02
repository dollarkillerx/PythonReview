# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 22:28 
# @Author : DollarKillerx
# @Description :

if __name__ == '__main__':
    list_a = []
    for i in range(10):
        list_a.append(i)
    c = map(lambda a:a*a,list_a)
    print(list(c))
