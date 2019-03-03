"""
11-14 我先用非闭包解决一下
"""

origin = 0

def go(step):
    new_pos = origin + step
    # origin = new_pos  这一步注释掉,就不会报错了
    return origin


print(go(2))
print(go(5))
print(go(11))

# UnboundLocalError: local variable 'origin' referenced before assignment

# 如果函数内部使用某个变量,而这个变量没有定义,会往上一级寻找.这里为什么报错,origin 没有赋值?
# 为什么下面不给 origin 赋值,就可以成功地从上一级得到变量?
# 因为 Python 把出现在等号左边的 origin 当作局部变量. Python 认为你既然有局部变量, 就不会去上一级寻找这个origin变量.
# 我们希望全局变量 origin 能够记住最新的坐标.


origin = 0

def go(step):
    global origin  # gloabal 关键字
    new_pos = origin + step
    origin = new_pos
    return new_pos


print(go(2))
print(go(5))
print(go(11))