"""
10-14 group 分组
"""
# 分组的概念在10-5提过，用括号将要重复的字符括起来。
# 分组不仅仅用于数量重复，还可以有其他作用。

import re

s = 'Life is short, I use Python'

# 提取 Life 和 Python 之间的字符：
# 定界

'''
r = re.search('Life\wpython', s)
print(r.group())

# 报错，没有匹配到。
# 为什么报错？ 因为 \w 只能表示一个字符，我们要加上重复。

'''

'''
r = re.search('Life\w*python', s)  # * 匹配前面的子表达式任意次。
print(r.group())

# 任然报错，因为空格不在单词字符中间。
'''

r = re.search('Life.*Python', s)  # . 匹配除“\n”和"\r"之外的任何单个字符。
print(r.group())

# Life is short, I use Python

# 但是我不要显示 Life 和 Python。
# 这个方法很重要，爬虫中我们经常需要根据HTML标签找到标签中间的内容。

r = re.search('(Life.*Python)', s)  # 添加()后变成一个分组。
print(r.group())

# Life is short, I use Python

# group 函数可以传入一个参数，指定你要获取的组号。这里我们只有一个组，可以不穿。

r = re.search('(Life.*Python)', s)
print(r.group(0))

# Life is short, I use Python

# group 函数的本质意义在于分组的匹配。

r = re.search('Life(.*)Python', s)
print(r.group(0))

# Life is short, I use Python

# group(0) 是一个特殊的情况，它永远记录正则表达式的完整结果。
# 如果想要访问完整匹配结果内某一个分组，必须从1开始访问。

r = re.search('Life(.*)Python', s)
print(r.group(1))

#  is short, I use
# 得到期望结果

# 使用 findall 更加简单
r = re.findall('Life(.*)Python', s)
print(r)
# [' is short, I use ']

# 返回 Life 和 Python 之间所有的字符。
# 找出两个 Python 之间所有的字符。
s = 'Life is short, I use Python, I love Python'

r = re.search('Life(.*)Python(.*)Python', s)  # 建立两个分组
print(r.group(0))
print(r.group(1))
print(r.group(2))

# Life is short, I use Python, I love Python
#  is short, I use
# , I love

print(r.group(0,1,2))  # 使用元组的方式返回三个组

# ('Life is short, I use Python, I love Python', ' is short, I use ', ', I love ')

print(r.groups())

# ' is short, I use ', ', I love ')

# groups() 只会把中间的匹配项返回给你。

r = re.findall(' .{0, 100} ', s)  # . 匹配除“\n”和"\r"之外的任何单个字符。
print(r)

