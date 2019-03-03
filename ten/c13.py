"""
10-13 search 与 match 函数
"""
import re

# re 模块里的其他方法：
# re.match
# def match(pattern, string, flags=0)
# re.search
# def search(pattern, string, flags=0)

s = 'A83C37D1D8E67'
r = re.match('\d', s)
print(r)
# None

# Why does it come out to be None?
# match 从字符串的开头开始匹配， 因为这个字符串的开始不是数字，所以返回没有匹配到任何结果。

r1 = re.search('\d', s)
print(r1)
# <re.Match object; span=(1, 2), match='8'>

# match 和 search 匹配结果不一样的原因是什么？
# match 从字符串的首字母开始匹配，如果 match 在首字母没有找到相应的匹配结果，将会返回None。
# search 搜索整个字符串，直到找到第一个满足正则表达式的结果，就将匹配结果返回回来。

s = '83C37D1D8E67'

r = re.match('\d', s)
print(r)
# <re.Match object; span=(0, 1), match='8'>

r1 = re.search('\d', s)
print(r1)
print(r1.group())  # 调用group()函数后可以拿到匹配的数字。
print(r.span())  # span() 方法返回正则表达式所匹配的结果在原字符串中的位置。
# <re.Match object; span=(0, 1), match='8'>
# 8
# (0, 1)

# 将字符串第一个字母去掉，match 和 search 返回的结果相同。
# 字符串首位是否是字母对 search 没有影响。

# match 和 search 与 findall 的不同：
# match 和 search 返回的结果比 findall 要复杂，他们返回的是对象。
# match 和 search 如果匹配成功将立刻停止搜索，并返回当前搜索结果。他们不会继续往后匹配。

r2 = re.findall('\d', s)
print(r2)
# ['8', '3', '3', '7', '1', '8', '6', '7']

# findall 可以将所有匹配结果打印出来。
# 更加推荐 findall。
