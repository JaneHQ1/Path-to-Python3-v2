"""
11-10 什么是闭包
"""

'''
def curve_pre():
    def curve():  # 函数里定义函数
        pass

curve()    

# NameError: name 'curve' is not defined

# curve 函数的作用域仅仅在于 curve_pre 函数的内部，在外部不能直接调用这样的局部函数。
'''

def curve_pre():
    def curve():  # 函数里定义函数
        pass
    return curve  # 函数是可以作为返回结果


f = curve_pre()
f()  # 现在f是一个函数，在后面加括号就可以执行这样的函数。

# 函数可以作为返回结果被其他函数返回回来。
# 可以把函数赋值给另外的变量f。

# 闭包的概念和变量的作用域有关。


def curve_pre():
    a = 25  # 局部变量 a 在 curve 的外部

    def curve(x):
        return a*x*x
    return curve


f = curve_pre()
print(f(2))

# 100


def curve_pre():
    a = 25  # 局部变量 a 在 curve 的外部

    def curve(x):
        return a*x*x
    return curve


a = 10
f = curve_pre()
print(f(2))

# 100

# 调用 f(2) 等价于调用 curve(2)。
# 变量 a 的值在 curve 函数里没有定义，会发生什么？
# 虽然 curve 函数没有执行，它只是作为定义返回到模块中，但是当我们在模块中调用 curve 的时候，a 并不会取模块中的变量，而是依然取它在定义时的环境变量。这就是闭包。
# 闭包的定义： 是由函数以及它在定义时候的外部环境变量所构成的整体。
# 一旦函数 curve 与变量 a 形成一个闭包之后，这个函数在任何一个地方调用的时候都不会受其他变量重新赋值所影响。它任然引用它的环境变量。
# 闭包 = 函数 + 环境变量
# 我的理解是这里的 curve 是一个环境变量,curve_pre 不是环境变量.
# 这里的环境变量一定在定义函数的外部。
# 如果 a 定义在 curve 内部，它就是返回了函数，并没有形成闭包。
# 这里的 a 不能是全局变量。

'''
a = 25  # a 是全局变量
def curve_pre():
    def curve(x):
        return a*x*x
    return curve

a = 10
f = curve_pre()
print(f(2))

# 40
# 这里没有形成一个闭包，所以 a 的值受影响了。
'''
# return curve 的时候不仅仅返回了一个函数，实际上返回的是一个闭包，也就是说它把函数和环境变量都返回回来。
# 我的理解:我们不能直接从外部调用闭包函数 curve, 于是我们 return 闭包函数.当我们在外部调用外部函数 pre_curve 后, 它可以返回闭包函数 curve.
# 如果没有 return curve 这个步骤, 我们根本不可能调用到闭包函数 curve.


print(f.__closure__)

# (<cell at 0x00000220DF3782E8: int object at 0x00007FFDF356B650>,)

# 在 Python 中，函数对象有一个__closure 属性。
# __closure__ 属性定义的是一个包含cell对象的元组，其中元组中的每一个 cell 对象用来保存作用域中变量的值。
# 如果没有形成闭包，则 __closure__ 属性为 None


print(f.__closure__[0].cell_contents)

# 25

# 返回环境变量的值

