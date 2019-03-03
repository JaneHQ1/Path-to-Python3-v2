"""
10-7 匹配0次1次或者无限多次
"""
import re

# 数量词

# {3,6} 数量词的一种表达形式
a = 'python1111java678php'
r = re.findall('[a-z]{3,6}', a)
print(r)
['python', 'java', 'php']

# * 匹配*前一位字符0次或者无限多次
a = 'pytho0python1pythonn2'
r = re.findall('python*', a)
print(r)
# ['pytho', 'python', 'pythonn']
# * 的作用是什么？
# 'pytho' 匹配了0次，所以出现在结果里。
# 'python' 匹配了1次。
# 'pythonn' 匹配了2次
# 也可以加在字符串中间。

# + 匹配+前一位字符1次或者无限多次
a = 'pytho0python1pythonn2'
r = re.findall('python+', a)
print(r)
# ['python', 'pythonn']
# 'pytho'不出现在列表中，因为n至少要出现一次。

# ? 匹配?前一位0次或者1次
a = 'pytho0python1pythonn2'
r = re.findall('python?', a)
print(r)
# ['pytho', 'python', 'python']
# 为什么结果出现了三个？
# 'pytho' 匹配了0次
# 'python' 匹配了1次
# 'pythonn' 匹配1次以后，多出的1个n会去掉。
# ? 经常用于去重。如果有很多重复的字符，只想保留0个或者1个，用字符串截取和循环都不是太好的办法，但是用 ? 就可以简单地解决这个问题。

# 如果了解正则表达式，就可以大幅度提高编码效率。
# 做数据处理，正则表达式把必不可少。

# ? 使用的场景及意义
# 非贪婪： ? 前面必须是一个范围，e.g.{3,6}?
# 匹配前一位0次或者1次：? 前面是固定的字符。
# 这两个模式是完全不一样的。

# 贪婪模式：寻找更多个n
r = re.findall('python{1,2}', a)
print(r)
# ['python', 'pythonn']

# 非贪婪模式：一旦找到一个n，就不会再找第二个n
r = re.findall('python{1,2}?', a)
print(r)
# ['python', 'python']
# 注意： 'python'是普通字符串，不是字符集，所以数量词{1，2}只是重复它前面一位n。

