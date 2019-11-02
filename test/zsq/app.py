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
    # return func


class ms:
    @staticmethod
    def test(name):
        def decorator(func):
            print("=============")
            return func

        return decorator


@decorator
def f1(name):
    print('this is a function', name)


@ms.test('name') # 默认会执行
def f2():
    print("this is f2")


if __name__ == '__main__':
    f1("sd")
    f2()
    # pass
