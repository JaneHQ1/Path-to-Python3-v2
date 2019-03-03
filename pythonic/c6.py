'''
    14-6 None
'''

# None 空
# 在类型上，None不等同于空字符串, 也不等同于空列表，也不等同于False
# 在取值上，也是不等同。
# 可以验证一下：
a = ''
b = False
c = []

print(a == None)
print(b == None)
print(b == None)

# 验证a和None有没有关联
print(a is None)

# False
# False
# False
# False

print(type(None))
# <class 'NoneType'>

# None是一个单独的类型
# 我们在做if判断的时候，经常会因为搞不清楚None，空列表，False，空字符串之间的关系，会造成一些误区。
# 在写代码的时候经常会对变量做判空操作。
# if not a
# if a is None
# 表面上看没有区别，但是实际上区别很大。

def func():
    return None

# a = func()
a = []

if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')

# S
# S

# Return None，都返回None，很容易误以为两个是等同的。

# S
# F
# a等于空列表，not a成立，但是a is None不成立
# 为什么？
# a is None: a是一个空列表，空列表不等同于None类型，所以判空操作是不对的。
# not a： 对空列表做逻辑运算，这个结果将会得到一个Bool。所以对于空列表来说，not a 最终的结果是True，所以打印'S'。
# 判空的时候不要混为一眼。
# 很多人喜欢用a is None 来探空。
# 推荐用 if a 和 if not 探空，下面的情况都可以得到想要的结果。
# a = None
# a = ''
# a = []
# a = False

# 从本质意义上理解None和False
# None 和 False 不是同一个类型， None是NoneType, False 是Bool。
# 本质意义上有什么不同？
# None是不存在的概念，False是真假。
# 很多情况下，if None 和 if False都能得到相同的结果。
# 但是结果相同不代表他们本质的概念和意义相同。
# 空列表表示列表里没有元素。
# 空字符串表示字符串没有元素。

# Summary
# None不是空字符串，空列表，False。
# 用 if a 和 if not 探空。


