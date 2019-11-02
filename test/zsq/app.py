# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 22:56 
# @Author : DollarKillerx
# @Description : 实现装饰器
import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


class ms:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            self.__func(*args, **kwargs)

        return wrapper()

    def test(self, name):
        print(name)


@decorator
def f1(name):
    print('this is a function', name)


@ms.test("name")
def f2():
    print("this is f2")


if __name__ == '__main__':
    f1("sd")
    f2()
    # pass
