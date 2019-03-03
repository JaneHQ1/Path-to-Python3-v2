"""
10-1 code
"""
# # 内置函数
# # Is 'Python' in the string below?
# a = 'C|C++|Java|C#|Python|Javascript'
# # Method 1：print True if 'Python' is in the string
# print(a.index('Python') > -1)
# # Method 2: print True if 'Python' is in the string
# print('Python' in a)


# 正则表达式
import re
a = 'C|C++|Java|C#|Python|Javascript'
# re.findall('正则表达式', '匹配的字符串')
r = re.findall('PHP', a)
print(r)
# if len(r) > 0:
#     print('字符中包含Python')

