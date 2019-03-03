"""
10-2 code
"""

# 正则表达式
import re
# 提取所有的数字
# for循环太麻烦,代码很复杂
a = 'C0C++7Java8C#9Python6Javascript'
# 有没有办法用抽象的方式把0到9表达出来
# r = re.findall('\d', a) # '\d' 表达0到9的数字
# print(r)

# 保留所有非数字D
r = re.findall('\D', a)  # 匹配一个数字字符
print(r)
