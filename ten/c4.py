"""
10-4 概括字符集
"""

import re
a = 'python1111java678php'
r = re.findall('\w', a)
# '\w' 匹配所有数字和字母
# print(r)

a = 'python1111java&678php'
r = re.findall('\w', a)
# '\w' 匹配不了&符号
# print(r)

r = re.findall('[A-Za-z0-9_]', a)
# print(r)

# '\W' 匹配非单词符号
a = 'python 1111java&678p\nhp'
r = re.findall('\W', a)
# print(r)

# '\s' 匹配之前特殊字符
a = 'python 11\t11java&678p\nh\rp'
r = re.findall('\s', a)
print(r)

# 常用概括字符集有三种:
# \d \D
# 单词字符集：\w \W
# 单词字符集范围：[A-Za-z0-9_]
# 空白字符集：\s \S
# 空白字符集例子：[' ', '\t', '\n', '\r']
# . 匹配除换行符之外其他字符
# Note:'&'不属于单词字符集和空白字符集
# * 匹配0次或者无限多次

