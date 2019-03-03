'''
    14-8 __len__与__bool__内置方法
'''

"""
class Test():
    def __bool__(self):
        return False
    
    def __len__(self):
        return 0
"""

# 这两个方法的返回结果将影响test对象最终的bool取值。
# 这两个方法如何影响最终的bool返回结果？
# __len__ 返回0，False
# __len__ 返回非0，True

"""
class Test():
    def __len__(self):
        # return '8'
        # return 1.0
        return True


print(bool(Test()))
"""
# TypeError: 'str' object cannot be interpreted as an integer
# TypeError: 'float' object cannot be interpreted as an integer
# True

# 不能返回字符串
# 不能返回浮点
# __len__ 返回True，True
# 如果Bool方法不出现，test的bool取值由len方法的返回结果决定。
# bool(Test())实质上是调用对象内部len的方法。
# 除了bool，len()也会调用对象内部的len。

# print(len(Test()))

# 1

# True 对应数字1

"""
class Test():
    pass


print(len(Test()))
"""
# TypeError: object of type 'Test' has no len()

# 如果没有私有len方法，无法对对象查长度。
# 不要对内置函数想得太神秘了,实质上是调用对象里的某一个方法.
# 不用全局方法也可以,实例化以后调用len方法也可以.
# 全局函数更加方便我们调用.
"""
class Test():
    def __len__(self):
        return 8

test = Test()

print(test.__len__())
"""
# 8

# 一旦我们加入bool方法,len的结果将不再影响整个对象的bool取值,而是由bool方法控制bool取值.

"""
class Test():
    def __bool__(self):
        # return False
        return 0

    def __len__(self):
        return True


print(bool(Test()))

# False
"""
# TypeError: __bool__ should return bool, returned int

# bool方法用0取代False会报错.
# 我们经常0,空字符串,空列表和False等同起来,但是类型不一样.
# 这里限定是bool类型就只能使用bool类型.


class Test():

    # Nonzero决定对象最终取值
    # 但是在Python3里Nonzero不能定义bool类型
    def __nonzero__(self):
        pass

    def __bool__(self):
        print('bool called')
        return False

    def __len__(self):
        print('len called')
        return True


print(bool(Test()))

# bool called
# False

# 有bool方法就不会调用len方法.
# 没有bool方法,len方法将会被调用.

