'''
    14-9 装饰器的副作用
'''

import time

'''
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    """
        This is f1
    """
    print(f1.__name__)


f1()
'''

# 使用装饰器之后对f1函数有什么影响?

# 不加装饰器:
# f1

# 加装饰器:
#1550833190.0967033
# wrapper

# wrapper 来自闭包函数
# 在某些情况下函数的名字被改变将会影响到我们的代码.

# 怎样可以增加装饰器之后，函数名不会被改变，依然保持原有函数名？
# Python提供了另外的装饰器来解决这个问题。


from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    """
        This is f1
    """
    print(f1.__name__)


f1()
help(f1)

# 1551241621.1712496
# f1
# Help on function f1 in module __main__:
#
# f1()
#     This is f1

# 实现了打印时间的功能
# 保留了原有名称
# 用f1()以后依然保留了f1函数的文档。

# 为什么wraps可以保持原有函数的不变?
# wraps装饰器接收了一个参数,这个参数就是原有函数f1
# wraps装饰器接收了原有函数,所以知道原有函数f1的信息
# 当我们去执行带装饰器的函数,我们实际上直接执行的是wrapper.
# 函数名字会丢失是因为我们直接执行的是wrapper,而不是f1.
# 借助wraps装饰器,可以把原有函数f1的一系列信息复制到wrapper闭包函数上,这样就可以保持原有的函数名.

