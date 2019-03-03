"""
11-12 闭包的经典误区
"""

def f1():
    a = 10
    def f2():
        a = 20  #定义f2之后，此时的a是否是环境变量？
        print(a)
    print(a)
    f2()
    print(a)  # 执行了f2之后，此时的a是10还是20？
              # 10，因为我们在f2外面执行a=10，将被Python认为是局部变量，局部变量是不能影响外部变量。


f1()

# 10
# 20
# 10

# 分析复杂的闭包函数，要从最外层逐步往里层分析。
# 这是一个闭包吗？

'''
f = f1()
print(f.__closure__)

# AttributeError: 'NoneType' object has no attribute '__closure__'

# f 是一个 None 类型，因为 f1 内部没有返回任何结果
'''

'''
def f1():
    a = 10
    def f2():
        a = 20
    return a

f = f1()
print(f.__closure)

# AttributeError: 'int' object has no attribute '__closure'

# int 类型没有 closure 属性
'''

def f1():
    a = 10
    def f2():
        a = 20
    return f2

f = f1()
print(f.__closure__)

# None

print(f)

# <function f1.<locals>.f2 at 0x0000026D5D234620>

# f 是一个function, 但是没有 closure 属性。

def f1():
    a = 10
    def f2():
        return a
    return f2

f = f1()
print(f.__closure__)
print(f1.__closure__)

# (<cell at 0x0000015BCF770108: int object at 0x00007FFDF861B470>,)
#  None

# 去除 f2 中 a 的值，closure 属性里就有值了。为什么？
# 因为如果 f2 里为变量 a 赋值， 此时 a 不再引用 f2 外部的环境变量，而是会被 Python 认为是一个局部变量。所以此时闭包就不存在了。
# 是否是闭包和 f2 返回结果无关。
# 这里的 a 不能当作变量去赋值，一定要去外部引用。