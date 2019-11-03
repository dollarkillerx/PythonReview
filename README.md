# Python Review
Py复习 Django真香

## 基本语法
- format
```python 
text = '{name} read {book}'.format(name='dollar',book='Py')

text = '{},ok ?'.format('ppp') 
```
- print
```python 
print('a',end=' | ') // end 结尾符
```
- 原始字符串
```python 
r"Newlines are indicated by \n"
```
- 显式行连接
```python
s = 'This is a string.\
This continues the string.'
print(s)
```
输出
```
This is a string.This continues the string.
```
### 项目结构
- 包
- 模块 (py 模块及类)
- 类
    * 函数,变量
包导入的顶级包 是与main执行文件所目录相关

### os
```python
def test1():
    inp = input("输入ppc:")
    f = open('cos.txt', 'w') # w写 r读 a追加
    f.write(inp)
    f.close()


def test2():
    f = open('cos.txt', 'r')
    a = f.read()  # 读全部
    print(a)


def test3():
    f = open('cos.txt','r')
    while True:
        line = f.readline() # 按行读
        if len(line) == 0:
            break
        print(line,end=' ')


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
```

### 异常
```python
def test_err():
    raise Exception('error') # 抛出异常


if __name__ == '__main__':
    try:
        test_err()
    except Exception:
        print(Exception)
    finally:
        print("end")
```

### 函数式编程
- lambda 表达式
```python
f = lambda x,y: x + y
f(1,2)
```
- 三元表达式
```python 
# true if 条件 else false
return x if x > y else y
```

### 装饰器
```python
# 定义装饰器
def decorator(func):
    def wrapper(*args,**kw):
        print(time.time())
        func(*args,**kw)

    return wrapper

@decorator
def f1(name):
    print('this is a function',name)

if __name__ == '__main__':
    f1("sd")
```
class 装饰器
```python
class ms:
    @staticmethod
    def test(name):
        def decorator(func):
            print("=============")
            return func

        return decorator

@ms.test('name') # 默认会执行
def f2():
    print("this is f2")
```
class 装饰器2
```python 
class Concurrent:
    @staticmethod
    def sync():
        def decorator(func):
            def war(*args, **kw):
                print("hello")
                func(*args, **kw)

            return war

        return decorator


# 下面是test
@Concurrent.sync()
def f1(name):
    print(name)


if __name__ == '__main__':
    '''
    this is test
    '''
    f1("hello")
```


### Py3.6 协程
https://www.cnblogs.com/hello-init/p/10375063.html

### 开始Django学习
- 基础 Django View Url Template ORM
- 扩展 Sqlalchemy Redis Mongodb Jinja2 Mako

### PipEnv
```bash 
pip3 install pipenv
pipenv install  # 带当前目录创建虚拟环境
pipenv shell    # 进入虚拟化环境
exit            # 退出虚拟环境
pipenv install  package   # 安装包
pipenv uninstall package  # 卸载包
pipenv graph    # 环境依赖
```
清华大学PIP源：https://pypi.tuna.tsinghua.edu.cn/simple/
### Django基础命令
- django-admin startproject 项目名称 -> 创建一个django项目
- python manage.py startapp 应用名 -> 项目中创建一个应用
- python manage.py shell -> 进入调试模式
- python manage.py makemigrations -> 数据库创建更改文件
- python manage.py migrate -> 同步到数据库进行更新
- python manage.py flush -> 清空数据库
- python manage.py runserver 0.0.000.0:8000 -> 启动开发服务器
- python manage.py 查看更多命令

### 基础入门
```bash 
pip3 install django
django-admin createproject project_name
cd project_name
django createapp app
django runserver
```
- app/views.py
```python 
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello")
```
- `touch app/urls.py`
```python 
from django.conf.urls import url
from .view import hello
urlpatterns = [
    url('',hello)
]
```
- project_name/urls.py
```python 
from django.contrib import admin
from django.urls import path, include

from app import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(app_urls))
]
```
## 参数获取
### Url参数获取
- 以?形式
```python 
request.GET.get(参数名称)
```
- 以分隔符信息
``` python
def index(request,参数名,参数名):
    print(参数名)
#   path('he/<str:name>/<int:age>',ppc)
```
- 获取POST类容
```python 
request.POST
```
- 获取path路径
```python 
request.path
```
- 获取请求方法
```python 
request.method
```
- 获取请求cookie
``` 
request.COOKIES
```
- 请求用户对象
``` 
request.user
```
- 获取session
``` 
request.session
```
- 获取meta
``` 
request.META
```
### 常用返回对象
- HttpResponse 可以直接返回一些字符串内容
- render 将数据在模板中渲染并显示
- JsonResponse 返回一个json类型
``` python
from django.http import HttpResponse
from django.http.shortcuts import render
from django.http impor JsonResponse
```
### 视图面向对象的写法
```python 
from django.views.generic import View
Class Test(View):
    def get(self,request):
        return xxx
# path('',Test.as_view())   调用
```

### Http常用返回状态码
- 200 ok
- 400 请求错误
- 401 未授权
- 403 权限不够
- 405 方法禁用
- 500 Server Error