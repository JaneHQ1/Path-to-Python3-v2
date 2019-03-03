'''
    14-5 iterator 与 generator
'''

# Python里组的表示方式：
# 列表、元组、集合

# 组的相关操作
# 可迭代对象(iterable)：
# 可以被for in循环来遍历的数据结构都是可迭代对象，e.g.列表，元组，集合

# 迭代器(iterator)：
# 迭代器是一个class。
# 假设自己定义一个class，可以被for in循环遍历吗？
# 不可以
# 那如何让自己定义的class被for in循环遍历？
# 将自己定义的class变成一个迭代器，就可以for in循环来遍历。
# 迭代器是可以被for in循环来遍历的，所以迭代器一定是一个可迭代的对象。
# 反过来说可迭代对象是迭代器，正确吗？
# 不正确
# 可迭代对象不一定是迭代器，比如说列表是可迭代对象，但不是迭代器
# 普通对象如何变成迭代器？
# 在普通对象下实现两个内置函数：
# def __iter__(self):
# def __next__(self):

"""
# 一组书是需要遍历
class BookCollection:
    def __init__(self):
        self.data = ['《家》', '《春》', '《秋》']
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

books = BookCollection()
for book in books:
    print(book)

# TypeError: iter() returned non-iterator of type 'NoneType'

# 现在这个class还不是迭代器，必须实现iter和next两个方法。

"""


class BookCollection:
    def __init__(self):
        self.data = ['《家》', '《春》', '《秋》']

        # 定义变量记录当前返回的序号
        self.cur = 0
        pass

    def __iter__(self):
        return self

    """
    for in 循环会不断调用迭代器里next方法，每调用一次，迭代器要返回一个数据。
    没有数据返回的时候，next需要抛出异常，表示这次迭代结束。
    """
    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        else:
            r = self.data[self.cur]
            self.cur += 1
            return r


books = BookCollection()
for book in books:
    print(book)

# 《家》
# 《春》
# 《秋》

# 还可以调用next方法,一个一个从迭代器里读取.
books2 = BookCollection()
# print(next(books2))
# print(next(books2))
# print(next(books2))

# 《家》
# 《春》
# 《秋》

# 不能对列表和元组使用next,因为列表和元组不是迭代器.
# 迭代器是一次性的.打印一次以后就不能再打印了.
# 如何多次遍历迭代器?
# 需要再次实例化新的BookCollection.
# 还可以用对象的拷贝,将books拷贝到另外一个对象上.

import copy
books = BookCollection()  # 不知道为什么这一行不能删

# 这里是一个浅copy
books_copy = copy.copy(books)

# 深copy
# books_copy = copy.deepcopy(books)

for book in books_copy:
    print(book)

# 列表和元组可以多次遍历.

# 生成器
# 打印0-10000数字
# 可以用列表推导式
"""
n = [i for i in range(0, 10001)]

for i in n:
    print(i)
"""
# 问题：消耗内存
# n是一个列表，列表消耗计算机内存。
# 有什么方法可以实现功能，但是又不需要数字存储在计算机里？
# 使用生成器
# 迭代器是针对一个class，生成器是针对一个函数。

# max是打印数字的上线
'''
def gen(max):
    n = 0
    while n<= max:
        print(n)
        n+=1

gen(10000)
'''

# 没有过度消耗计算机的内存，因为每一次打印都是实时算出来的结果，并不是把数字存储起来再打印。
# 但这只是普通的函数，不是生成器。
# 这个函数的问题是实现的目的太过特殊，它在函数的内部直接把数字打印出来。
# 如果最终目的是为了得到这些数字，然后用这些数字去做别的事情，该怎么办？
# 我们在函数的外部调用函数的真实目的在于希望函数返回0-10000的数字。我怎么用不需要它管。就算打印我也在函数外部打印。
# 所以这个函数解决了性能问题，但是不满足要求。

"""
def gen(max):
    n = 0
    while n<= max:
        # print(n)
        n+=1
        return n

print(gen(10000))

# 1
"""
# 如果我们取消内部打印，直接在函数return n，最后只打印了1，为什么？
# 当我们在函数内部调用了return语句，整个函数的调用语句就结束了，根本就不会进行下一次的while循环。
# 怎么解决这个问题?
# 我们把return改成yield。
"""
def gen(max):
    n = 0
    while n<= max:
        # print(n)
        n+=1
        yield n

print(gen(10000))

# <generator object gen at 0x000002623DFC28B8>
"""
# 结果得到一个生成器。
# 生成器怎么用？
# 有两种用法：


# 一 用next调用
def gen(max):
    n = 0
    while n<= max:
        # print(n)
        n+=1
        yield n

g = gen(10000)
print(next(g))
print(next(g))
print(next(g))

# 1
# 2
# 3

# 二 用for in 循环进行遍历
for i in g:
    print(i)

# 生成器的优势:
# 既保证了函数的通用性,又解决了性能问题.
# 在生成器的内部我们没有保存任何数据.
# 生成器内部保存了算法.
# 保存算法不会占内存.
# 但是通过这个算法不断地在for in循环里取生成新的数字.

# yield 作用:
# 当第一次调用next,生成器进入while循环,一旦遇到yield之后,就像return一样,会把值返回出去.
# 一旦函数遇到return之后,整个函数执行流程结束,但是yield不会.
# 第一次调用next,yield返回n出去.第二次调用next,yield会接着第一步,继续执行while循环.
# 如果把yield换成return,那么这里就是一个普通的函数,不是生成器.
# 之前用列表推导式得到的是一个列表,其实是可以得到一个生成器的.

# 把中括号改成圆括号
n = (i for i in range(0, 10001))
print(n)

# <generator object <genexpr> at 0x00000209117029A8>

# 现在n就不是列表,而是一个生成器.

