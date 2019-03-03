"""
11-9 一切皆对象
"""

# 高级知识很多与函数式编程的概念是相关的。
# 本课程不讲函数式编程的理论知识，因为函数式编程没有标准定义。
# 七月老师对函数式编程的理解是不断变化的。
# 函数式编程的定义不是很重要，重要的是懂得用函数式编程的思维帮助你解决问题。
# 函数式编程并不是必须的。只是为了简化代码，写出优质的接口。
# Python支持函数式编程，但并不一定要用。
# 代码非常繁琐，别扭，可以思考一下有没有别的编码的思路。
# 淡化函数式编程的概念。
# Python高阶的知识比面向对象更抽象。
# 高阶函数的难度不在于你听不听得懂，而在于你听懂了会不会用。
# 有编程经验再来听感触会比较深刻。

# 闭包
# 不是Python独有的，闭包的概念在JS里出现地比较多。
# 闭包与函数是有关系的。
# 在Python里，函数是一个对象，可以实例化。
# 在其他语言里，函数只是一段可执行的代码，并不是对象。函数一经编译就固化了，我们只要获得函数的入口就可以调用函数。
# 在其他语言里，函数是不可以实例化的，它只是一段可执行的代码常驻于内存中。
# 在C#中，除了类和对象，还有结构等很多种类型。
# Python一切皆对象，所有在Python中出现的东西都可以当作对象的行为来理解。
# Python中一切皆对象的好处：
# 可以把数值或者字符串赋值给变量a，因为一切皆对象，你能赋值字符串，也可以把函数赋值给变量的。但是在C#里想把函数赋值给一个变量是做不到的。
'''
a = 1
a = '2'
a = def
'''
# Python可以把函数赋值非变量。
# Python可以把函数当作参数传递到另外一个函数。
# Python可以把一个函数当作另外一个函数的返回结果返回到调用方。

# C#里，想把一个函数当作参数去传递，需要把函数封装成委托。

# Python一切皆对象的概念让它可以进行函数式编程或者做闭包打下了坚实的基础。

def a():
    pass

print(type(a))

# <class 'function'>

# a的类型是function。


# 函数可以被赋值给变量
def hello(name='world'):
    print('hello ' + name)

# my_func = hello
# my_func('python')

# 类可以被赋值给变量
class Person:
    def __init__(self):
        print('__init__')

# my_class = Person
# my_class()

# 可以添加到集合对象中

# 定义集合对象
obj_list = []
# 添加方法与类到几个中
obj_list.append(hello)
obj_list.append(Person)

# for item in obj_list:
#     print(item())

## 可以作为参数传递给函数
def print_type(item):
    print(type(item))

# for item in obj_list:
#     print_type(item)


# 可以当做函数返回值
def decorator_func():
    print('调用decorator_func函数')
    return hello

my_func = decorator_func()
my_func('python')
