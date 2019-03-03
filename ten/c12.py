# -*- coding: utf-8 -*-
"""
10-12 把函数作为参数传递实例

Created on Fri Feb  1 19:59:02 2019

@author: janej
"""

import re

# 替换条件：
# 找出字符串中所有的数字
# >=6 替换为9
# <6 替换为0

'''
# s = 'A8C3721D86'

# def convert(value):
#    num = value.group()
#      print(type(num))  # 这里的num实际上是string
#    if int(num) >= 6:  #需要转型成int
#        return '9'  # 不能直接返回int，因为正则表达式只能操作字符串
#    else:
#        return '0'
#
#r = re.sub('\d', convert, s)
#print(r)
'''
# A9C0900D99

# 如果参数不能接收函数， 这个if-else逻辑不能写到sub里。

"""
    从软件设计角度思考convert函数的意义
"""

# 我作为sub函数的编写方，有一些逻辑是无法帮你做决定的，
# 于是我开放一个接口，让你自己去实现一些逻辑功能，
# 我要求你给我传入一个函数，我把你的函数作为参数接收之后，就可以在sub函数内调用你的convert
# 我在调用的时候就会给你一个中间的结果value，随便你怎么处理这个value，但是最终你要还给我一个字符串
# 这样的设计方式非常灵活
# 我们自己编写函数的时候可以模仿这个做法

# 这个例子是简单地匹配单个字符，如果我们做一个模糊的匹配，那么for循环就不能实现了。

# e.g.
# 匹配条件：
# 先剔除单个数字
# 再以两位数字为整数进行判断
# >50 替换成100
# <50 替换成0

# 对于这个例子，for循环也能写出来，但相比正则表达要复杂很多

def convert(value):
    num = value.group()
    if int(num) >= 50:
        return '100'
    else:
        return '00'

s = 'A8C3721D86'

# r = re.sub('\d{1,2}?', s)
r = re.findall('\d{2}', s)
print(r)
r = re.sub('\d{2}', convert, s)
print(r)


