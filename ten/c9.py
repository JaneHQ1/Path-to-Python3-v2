"""
10-9 组
"""
import re

a = 'PythonPythonPythonPythonPython'

# 判断字符串中是否包含3个Python
r = re.findall('PythonPythonPython', a)
print(r)
# ['PythonPythonPython']
# 这样是可以的，但如果判断是否包含100个，这样做就不现实了。

# 用() 将一系列字符成为一个组，再在一组字符后面加上数量词，代表将这一组字符重复若干次。
r = re.findall('(Python){3}', a)
print(r)
# ['Python']
# 匹配失败显示[]

# 一个正则表达式是可以包含多个组。
a = 'PythonPythonPythonPythonPythonJS'
r = re.findall('(Python){3}(JS)', a) # 包含两个组(Python)和(JS)
print(r)
# [('Python', 'JS')]

# [] 和 () 逻辑上有什么不同？
# [abc] a|b|c
# (abc) a&b&c

