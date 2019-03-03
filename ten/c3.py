"""
10-3 字符集
"""

import re
s = 'abc, acc, adc, aec, afc, ahc'

# 找出单词中间字符是c或者是f的单词
# 用字符集
r = re.findall('a[cf]c', s)
print(r)

# 找出单词中间不是c或者f的单词
r = re.findall('a[^cf]c', s)
print(r)

#如果匹配的字符太多，可以利用字符的顺序，来省略中间的字符。
# 匹配c到f
r = re.findall('a[c-f]c', s)
print(r)