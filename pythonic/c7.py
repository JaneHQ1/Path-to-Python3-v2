'''
    14-7 对象存在不一定是True
'''

a = ''

# if a 和 if None 的分支是相同的。为什么？
# if 逻辑判断，Python里每个对象都和Bool有对应关系。
# True False 对应关系：
# ''   False
# []   False
# None   False
# 几乎所有的对象和True和False相关。
# 那我们自定义的对象如何定义？

'''
class Test():
    pass


test = Test()

# 探空
if test:
    print('S')

# S
'''
# 思路：
# 如果Test存在，不是空值，if Test 是成立的。
# 有没有可能Test不是None，但依然是Test类实例化的对象，但最终if test不会打印出'S'

class Test():
    # 让Test长度为0
    def __len__(selfs):
        return 0


test = Test()

# 探空
if test:
    print('S')
else:
    print('F')
    
    
# F

# 探空上习以为常的逻辑误区。
# 永远不要认为对一个对象做if else判断操作一定到if分支，即使取值不是None，它也依然有可能进入else分支。

print(bool(None))
print((bool([])))
print(bool(test))

# False
# False
# False

# test的Bool类型是False，所以进入else分支。


class Test():
    # 让Test长度为0
    pass


test = Test()
print(bool(test))

# True

# 如果Test里没有len方法，test对象变成了True
# 几乎所有的Python对象在做if判断都和Bool之间有转换关系。
# 对于自定义对象来说，千万不要认为test存在他一定是True。
# test存在也有可能是False.
# 自定义对象怎么判断True还是False？
# 和它内部定义的两个方法有关系。
# 一 __len__
# 二 __bool__
# 这两个方法如何影响test对象的bool取值请听下回分解。

