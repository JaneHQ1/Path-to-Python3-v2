"""
11-15 再用闭包解决一下
"""

origin = 0


def factory(pos):
    def go(step):
        new_pos = pos + step
        # pos = new_pos  pos被认为是局部变量
        return new_pos
    return go


tourist = factory(origin)
# print(tourist(2))
# print(tourist(5))
# print(tourist(11))

# UnboundLocalError: local variable 'pos' referenced before assignment

# 使用闭包也会出现局部变量的问题. 怎么解决?
# 强制声明 pos 不是局部标本量


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
# print(tourist(2))
# print(tourist(5))
# print(tourist(11))

# 2
# 7
# 18

# 非闭包和闭包的执行区别:
# 非闭包的执行是利用全局变量的特性.
# 闭包使用的是环境变量.
# 闭包的环境变量有保存现场的功能, 它可以记忆上一次调用的状态.

# <代码大全II> 尽量少得使用全局变量
# 没法保证其他函数不会改变全局变量, 这会导致函数没有自封闭性,非常容易受其他函数影响.
# 闭包函数并没有直接使用全局变量 origin.
# 闭包函数的优势:没有改变全局变量, 所有的操作都局限于函数的内部.

print(tourist(2))
print(tourist.__closure__[0].cell_contents)
print(tourist(5))
print(tourist.__closure__[0].cell_contents)
print(tourist(11))
print(tourist.__closure__[0].cell_contents)

# 2
# 2
# 7
# 7
# 18
# 18

# 证明闭包记住了之前的状态.