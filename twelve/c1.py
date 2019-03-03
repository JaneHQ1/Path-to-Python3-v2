"""
12-1 lambda 表达式
"""

# 匿名函数/ lambda 表达式
# 定义函数的时候不需要定义函数名。
# 函数的基本定义：


def add(x,y):
    return x+y

# 匿名函数
# lambda parameter_list: expression

# 学习匿名函数最好的方式：对比普通函数一起学习。
# lambda 后面的 expression 只能是一些简单的表达式，不能完整地实现函数内部的代码块。


lambda x, y: x+y  # add 函数使用匿名函数实现

# 匿名函数与add函数的区别：
# 匿名函数没有 add 名字
# 不需要 return 语句返回。冒号后边 expression 表达结果就是匿名函数的返回结果。

# 如何调用匿名函数？匿名函数没有名字，我们怎么调用？
# 虽然匿名函数没有名字，但是我们可以将匿名函数赋值给一个变量。
# 赋值给变量之后我们就可以调用

f = lambda x, y: x+y
print(f(1, 2))
print(add(1, 2))

# 3
# 3

# 匿名函数和普通函数实现的效果一样的。但是匿名函数的定义非常简洁。
# 目前为止调用匿名函数的方式并没有体现匿名函数的优势。
# 正则表达式中有个地方特别适合匿名函数.
# 在 Python 里, lambda 称为匿名函数.
# 在 C# 里, lambda 定义的函数成为 Lambda 表达式，关键点在表达式上.后面只能是表达式,不能是代码块.

# f = lambda x,y: a = x+y

# SyntaxError: can't assign to lambda

# 不能在 lambda 做赋值操作, 因为我们强调了冒号后面只能是表达式, a = x+y 不是表达式,是完整的代码语句.
# Python 里匿名函数突出表达式更合适.
# C# 里匿名函数和 lambda 表达式是两个不同的东西.

# Summary
# 匿名函数/ lambda 表达式
# lambda parameter_list: expression
# expression 只能写表达式，不能写代码块。
