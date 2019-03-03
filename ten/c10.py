"""
10-10 匹配模式参数
"""
import re

language = 'PythonC#JavaPHP'

# re.findall('正则表达式', '匹配的字符串', '匹配模式')
# re.findall('pattern', 'string', 'flags')
r = re.findall('c#', language)
print(r)
# []
# 匹配不了，因为 c 和 C 不是相同得字符。

# 如何忽略大小写？
r = re.findall('c#', language, re.I)
print(r)
# ['C#']
# re.I 只是好几种模式中的一种。

# flag 参数可以接收好几种模式，多个模式中间用 | 连接在一起。
r = re.findall('c#', language, re.I | re.S)
print(r)
# ['C#']

# re.S 的作用：
# 改变. 的行为让它可以匹配换行符 \n

# 不加 re.S
language = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}', language, re.I)
print(r)
# []
# 概括字符集. 匹配除换行符 \n 之外其他所有字符。
# c#.{1}: 首先匹配c#，然后匹配任意的字符包括 \n
# . 不能匹配 \n， 所以正则表达式不成功。

# 加上 re.S
r = re.findall('c#.{1}', language, re.I | re.S)
print(r)
# ['C#\n']

# Note：re.I | re.S 形式上很像 or ，但是这里是 and 关系。

