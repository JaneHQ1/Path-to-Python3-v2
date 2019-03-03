"""
12-6 filter
"""

# filter 可以过滤掉一些我们不需要的元素。
# 或者说帮助我们过滤掉一些不符合我们定义规则的元素。
# class filter(function or None, iterable)

list_x = [1, 0, 1, 0, 0, 1]

# 剔除数值为0的元素。

r = filter(lambda x: True if x==1 else False, list_x)
print(r)

# <filter object at 0x00000225D2F62438>

print(list(r))

# [1, 1, 1]

# filter 的特点在于 lambda 表达式上。
# lambda 表达式要求必须返回结果必须是 True 或者 False，或者代表真和假。
# 之前的例子可以省略 if else， 因为1和0也代表 True 和 False。

r = filter(lambda x: x, list_x)
print(list(r))

# [1, 1, 1]

# lambda 表达式判断出真假就可因,因为 filter 就是靠函数的返回结果来判断当前元素是否应该保留在集合里.
# 如果返回 false, 当前元素会从当前集合剔除出去.

# filter 特别适合做集合的过滤.

list_u = ['a', 'L', 'c', 'O', 'e', 'V', 'g', 'E']

# 过滤掉所有小写,只保留大写

r = filter(lambda x: x.isupper(), list_u)
print(list(r))

# ['L', 'O', 'V', 'E']

# Summary
# filter 可以过滤掉一些我们不需要的元素。
# class filter(function or None, iterable)
# lambda 表达式要求必须返回结果必须是 True 或者 False，或者代表真和假。