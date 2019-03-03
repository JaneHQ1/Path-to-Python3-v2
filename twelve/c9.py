"""
12-9 装饰器 二
"""

# 用装饰器解决上节课的问题。
# 装饰器只是一种模式。
# 我们所用的装饰器就是用之前学到的知识点。

import time


def decorator(func):
    # 要实现装饰器需要用到之前学到的嵌套函数定义的方式。
    def wrapper():
        print(time.time())
        func()
    return wrapper
# 有点类似之前学习的闭包。


def f1():
    print('This is a function')


def f2():
    print('This is a function')

f = decorator(f1)
f()

# 1550487602.0629954
# This is a function

#  这个装饰器和之前的函数有什么区别？
# 唯一的区别是我们把Print_current_time 函数封到了内部。
# 这样的写法内聚性更高。

# 为什么这样的写法叫做装饰器？
# 真正的业务逻辑在 wrapper 里。
# 我们通过 wrapper 外面包裹一层 decorator 来实现我们不改变原有的函数而增加新的功能的特性。
# 看起来就像 wrapper 被 decorator 装饰了一样。

# 上节课的定义方式最不好的地方在于，定义函数没有体现出和原来f2的关联性。
# f2依然是一个独立函数，并没有和新增加的功能关联起来。
# 这节课只是变了一个花样，但任然没有解决上一节课的问题。




