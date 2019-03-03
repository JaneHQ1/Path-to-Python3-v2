"""
11-5 枚举注意事项
"""
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 1  # YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4

print(VIP.GREEN)

# VIP.YELLOW

# print GREEN,输出是 YELLOW
# 两个枚举类型赋值相同,实际上是代表一种枚举类型,我们把第二个类型 GREEN 看作是 YELLOW 的别名.不能看作一个单独的枚举类型.

# 枚举的类型相等，枚举的遍历会有什么不同？
for v in VIP:
    print(v)

# VIP.YELLOW
# VIP.BLACK
# VIP.RED

# VIP.GREEN 没有打印出来，因为 GREEN 不是独立的枚举类型，它被 Python 视作 YELLOW 的别名。

# 如何将别名遍历出来？
for v in VIP.__members__.items():
    print(v)

# ('YELLOW', <VIP.YELLOW: 1>)
# ('GREEN', <VIP.YELLOW: 1>)
# ('BLACK', <VIP.BLACK: 3>)
# ('RED', <VIP.RED: 4>)

# 使用 items() 方法得到的结果都是元组。

for v in VIP.__members__:
    print(v)

# YELLOW
# GREEN
# BLACK
# RED

# 不用 items() 方法，得到精简的类型名称。
