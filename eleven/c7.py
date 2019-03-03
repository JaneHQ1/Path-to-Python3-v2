"""
11-7 枚举小结
"""
from enum import Enum
from enum import IntEnum,unique

# 之前的事例每一个枚举类型取值都是数字，但是实际上也可以用字符串。
# 但是如果我们强制要求枚举类下面的每一个枚举类型都是数字，不允许用字符串，就可以继承IntEnum。

'''
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 'str'
    BLACK = 3
    RED = 4
    
# ValueError: invalid literal for int() with base 10: 'str'
'''

# 如果想限制每个枚举类型不能取相同的值
'''
@unique  #装饰器
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4

# ValueError: duplicate values found in <enum 'VIP'>: GREEN -> YELLOW
'''

# 这是枚举类和普通类的区别：枚举类在 Python 中实现单例模式，是不能实例化的。
# 设计模式是为了解决软件工程里面频繁变化的一个问题而产生的解决方案。
# 在实践中学习设计模式。
# 设计模式不是必须的。
# 设计模式是为了避免代码频繁地变化。

