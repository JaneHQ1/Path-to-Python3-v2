"""
12-12 装饰器 五
"""
import time

# 继续优化装饰器：


def decorator(func):
    def wrapper(*args, **kw):  # 这里kw可以用任何名字，这是一个形参。
        print(time.time())
        func(*args, **kw)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function: ' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is a function: ' + func_name1 + ' ' + func_name2)


@decorator
def f3(func_name1, func_name2, **kw):
    print('This is a function: ' + func_name1 + ' ' + func_name2)
    print(kw)  # 可以将kw作为字典打印出来

# f3 增加了关键字参数。
# TypeError: wrapper() got an unexpected keyword argument 'a'
# *args不能兼容关键字参数。
# 在wrapper里增加关键字参数。

f1('test func')
f2('test func1', 'test func2')
f3('test func1', 'test func2', a=1, b=2, c='123')

# 1550491846.4074614
# This is a function: test func
# 1550491846.4074614
# This is a function: test func1 test func2
# 1550491846.4074614
# This is a function: test func1 test func2
# {'a': 1, 'b': 2, 'c': '123'}

# 现在decorator的形态是一个完整的装饰器形态。

# 小技巧
# func(*args, **kw)
# 在python里如果有这样的调用形式，不管函数有多少个参数和关键词参数。
# 在不确定函数参数的情况下都可以用这种方式调用。
# 建议使用明确的传参。
# 但有的时候写比较抽象的函数，不知道参数应该传什么，可以使用这个方式。

