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

### Pickle 
