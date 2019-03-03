"""
12-5 reduce
"""

# Python3 的 reduce 不在全局的命名空间里。

from functools import reduce

# def reduce(function, sequence, initial=None)
# reduce 下的两个函数必须有两个参数。

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

r = reduce(lambda x, y: x+y, list_x)
print(r)

# 36

# 在 reduce， lambda 表达式有参数 y，但是我们没有传入y。y 从哪里来？

# reduce 的运算原理和规则：
# reduce 在做连续的计算。
# reduce 会连续调用我们定义的 lambda 表达式。
# (1+2)+3)+4)+5)+6)+7)+8)= 36
# 每一次 lambda 表达式的计算结果将作为下一次 lambda 表达式的参数进行运算，直到 list_x 被遍历完。
# reduce 对执行流程非常抽象。

# Python 有内置的求和函数。但是有些功能没有内置函数，还是需要reduce去执行。
# 旅行者的坐标，用坐标点(x,y)表示旅行者的位置。
# 用列表记录每一次的移动。

origin = (0, 0)
move = [(1, 3), (2, -2), (-2, 3)]  # 移动的坐标
x = 0
y = 1

# 计算最终旅行者的位置：

current_location = reduce(lambda pre_step, next_step: (pre_step[x]+next_step[x], pre_step[y]+next_step[y]),
                          move, origin)

print(current_location)

# (1, 4)

# reduce 不仅仅做连续相加，它是做连续计算的。reduce 做什么计算取决于 lambda 表达式。

# reduce 增加 initial：

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

r = reduce(lambda x, y: x+y, list_x, 10)
print(r)

# 46

# 比原来的结果增加了10.
# 第一次计算的时候，10作为初始值参与到运算，并不是最后相加的。
# （10+1）+2)+3)+4)+5)+6)+7)+8)= 46

# 拓展
# 谷歌大数据模型：map/reduce
# map/reduce在大数据计算里是一个编程模型。
# map 映射
# reduce 归约
# map/reduce 在大数据里最主要的运用是并行计算。
# map/reduce 的思想就是从函数式编程里借鉴的。
# Python 里函数式编程最主要的体现就是在 map/reduce 上。

# Summary
# def reduce(function, sequence, initial=None)
# reduce 下的两个函数必须有两个参数。
# reduce 做的是连续的计算。
# reduce 做什么计算取决于 lambda 表达式。
