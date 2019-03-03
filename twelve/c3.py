"""
12-3 map
"""

# 不推荐在业务代码里大量使用闭包.
# 在框架,包或者类库里,可以尝试使用闭包.

# 函数式编程另一个非常典型的概念和用法,推荐多多使用:
# 通过 map class 完成
# class map(func, *iterables)
# 两个参数: 函数, 一个序列或者一个集合
# map 类使用场景:
# 求列表中每个数字的平方,并且把每个数字的平方再组成一个新的列表.将新的列表打印出来

list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x


for x in list_x:
    # 通过循环实现
    square(x)

# 如何用 map 实现?
r = map(square, list_x)

# map 的结果是 object
print(r)

# <map object at 0x0000013592E291D0>

print(list(r))

# [1, 4, 9, 16, 25, 36, 49, 64]

# map 的基本用法:
# map 会对传入的集合或者序列的每一项都执行 square函数.
# 换言之,调用 map 以后, map 会把集合里每一个元素都传到 square 里去, 并且会接收 square 的返回结果.
# 可以当作执行了一个 for 循环, for 循环内部都执行了 square 函数.

# 从数学的层面看, map 就是映射.它将集合里的每一个元素都映射到新的集合里去.
# 最终的映射结果是函数所决定的.

# Summary
# class map(func, *iterables)
# 可以将 map 理解为映射。
