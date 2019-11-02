# -*- coding: utf-8 -*- 
# @Time : 2019-11-02 20:26 
# @Author : DollarKillerx
# @Description :

class Person:
    '''
    用户Class
    '''
    name = "这个是构造函数"

    def __init__(self):
        '''
        this is 构造函数
        '''
        print("构造函数")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        '''
        获取名称 先会查询self变量 如果 没有 就去查询类变量
        '''
        return self.name

    @classmethod  # 类方法
    def how_many(cls):
        print(cls.name, '哈哈哈')

    @staticmethod  # 静态方法
    def stat():
        print("static method")


def test1():
    p = Person()
    p.set_name("你好呀")
    print(p.get_name())
    Person.how_many()

    Person.stat()


class SchoolMember:
    def __init__(self, name):
        self.school = name

    def graduated_school(self):
        return self.school


class Student(SchoolMember):
    def __init__(self, name, school):
        super().__init__(school)
        self.name = name

    def get_name(self):
        return self.name


if __name__ == '__main__':
    # test1()
    student = Student("dollarKiller", "电子科技")
    print(student.get_name())
    print(student.graduated_school())
