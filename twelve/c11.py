"""
12-11 装饰器 四
"""

# 假如说函数f1需要接收多个参数，这个装饰器需要做那些改变才能支持带参数的函数？

# 带一个参数的情况：

import time

'''
def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def f1(func_name):
    print('This is a function, named' + func_name)


f1('test func')

# TypeError: wrapper() takes 0 positional arguments but 1 was given

# 因为里面封装函数wrapper没有参数。

'''

'''
def decorator(func):
    def wrapper(func_name):
        print(time.time())
        func(func_name)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function: ' + func_name)


f1('test func')

# 1550490478.046214
# This is a function: test func

'''


def decorator(func):
    def wrapper(*args):  # args在很多编程语言里代表一组参数，没有具体意义。
        # 在实际业务里给函数参数列表去把名字就不要叫args,应该取一个和业务相关，有具体意义的名字。
        print(time.time())
        func(*args)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function: ' + func_name)


@ decorator
def f2(func_name1, func_name2):
    print('This is a function: ' + func_name1 + ' ' + func_name2)


f1('test func')
f2('test func1', 'test func2')

# 1550491205.9946356
# This is a function: test func
# 1550491205.9946356
# This is a function: test func1 test func2

# 装饰器具有特定性，可以在多个函数上通用。
# 如果一个装饰器绑定在一个函数上，就没有意义了。
# 利用Python函数可变参数的特性解决这个问题。
# 我们给的是可变参数，所以可以传入任意参数。


