"""
10-11 re.sub正则替换
"""

import re

language = 'PythonC#JavaPHP'

"""
    替换字符串
"""
# 之前学习的都是查找字符串，如何实现查找之后替换？

# re.sub(pattern, repl, string, count=0, flags)
# pattern：正则表达式
# repl：匹配成功以后需要替换成的字符串
# string: 需要搜索的原字符串
# flags： 匹配模式
# count: 匹配之后所能被替换的最大次数

r = re.sub('C#', 'Go', language)
# print(r)

# PythonGoJavaPHP

language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#', 'Go', language)
# print(r)

# PythonGoJavaGoPHPGo

r = re.sub('C#', 'Go', language, 1)
# print(r)

# PythonGoJavaC#PHPC#

# 只有第一个C#被替换成GO

"""
    字符串内置函数 replace （正则表达式sub的简化版）
"""
# def replace(old, new, count = None)

language.replace('C#', 'GO')
# print(language)

# PythonC#JavaC#PHPC#

# 为什么 language 在执行 replace 函数之后并没有执行替换？
# 因为字符串不可变，如果要实现替换，需要新生成一个字符串。

language = language.replace('C#', 'GO')
# print(language)

# PythonGOJavaGOPHPGO

# 常规的替换可以用replace，比较简单
# 内置函数可以实现的查找或者替换逻辑，正则表达式肯定可以实现
# 内置函数无法实现的功能，正则表达式也可以实现

"""
    re.sub高级用法
"""

# 第二个参数可以是一个函数
# 这种函数的形式Python使用非常多，不仅仅用在正则表达式，包括salt排序也会使用
'''
def convert(value):

#   return '!!' + value + '!!' 

#   直接 return 会报错

    print(value)


language = 'PythonC#JavaC#PHPC#'

r = re.sub('C#', convert, language)
           
print(r)
'''

# <re.Match object; span=(6, 8), match='C#'>

# <re.Match object; span=(12, 14), match='C#'>

# <re.Match object; span=(17, 19), match='C#'>

# 有三个C#，所以convert被调用了三次
# 如果C#能够匹配到，那么C#将会作为参数传递到函数convert里
# convert的返回结果将会替换C#
# Note: value 传递的并不是字符串, 而是对象

# 重点：
# 通常情况下我们只需要拿到正则表达式匹配的结果C#，但是Python除了给我们字符串意外，还会有额外的信息。
# span: 当前匹配的正则表达式在元字符串的位置
# span=(6, 8) c#前面有6个字符，自己占用第7，8位

""" 
    如何从返回对象中拿到C#字符串？ 
"""

def convert(value):
     matched = value.group()
     return '!!' + matched + '!!' 
 
language = 'PythonC#JavaC#PHPC#'
r = re.sub('C#', convert, language)          
print(r)
# Python!!C#!!Java!!C#!!PHP!!C#!!
 
# 这样的形式非常有意义
# 替换的结果不只是普通字符串，可能有各种各样的结果
# 有时候需要根据不同的匹配结果，做不同的替换操作，
# 如果没有没有函数的支持，这个功能很难实现，
# 把函数当作参数传到sub函数，就可以把判断的工作交给函数处理
# 函数的参数列表接收另外的函数是Python是Python非常强大的地方

def convert(value):
    get_span = value.span()
    print(get_span)


language = 'C#PythonC#JavaC#PHPC#'

r = re.sub('C#', convert, language)
           
print(r)



