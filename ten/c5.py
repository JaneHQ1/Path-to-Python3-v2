"""
10-5 数量词
"""
import re
# 把字符串中所有单词匹配出来
# [a-z]可以把所有字符匹配出来，但是并不是以单词的形式出现。
a = 'python 1111java678php'
r = re.findall('[a-z]', a)
print(r)

# 连续几个字符集可以让结果成组，但是单词字符太多就不现实
r = re.findall('[a-z][a-z][a-z]', a)
print(r)

# [a-z][a-z][a-z]等同于[a-z]{3}
# {3,6}表示数量词前面的字符集重复3到6次
r = re.findall('[a-z]{3,6}', a)
print(r)

# 这个例子里，匹配到3个以后已经可以完成匹配。
# 为什么正则表达式在匹配到3个以后任然会继续匹配？
# 这个涉及到正则表达式数量词的一个非常重要的概念。
