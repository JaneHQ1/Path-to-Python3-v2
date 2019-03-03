"""
10-3 枚举类型,枚举名称与枚举值
"""
from enum import Enum

# 枚举相关的操作:

# 操作一:
# 如何获得枚举类型下某一个标签对应的具体数值?

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.GREEN.value)

# 2

# 如何获得枚举类型下标签的名字?
print(VIP.GREEN.name)

# GREEN

# 以下两个print有什么区别?
# print(VIP.GREEN)
# print(VIP.GREEN.name)

print(type(VIP.GREEN))
print(type(VIP.GREEN.name))

# <enum 'VIP'>
# <class 'str'>

# print(VIP.GREEN)       枚举类型
# print(VIP.GREEN.name)  枚举类型下标签的名字
# print(VIP.GREEN.value) 枚举类型下标签对应的具体取值

print(VIP['GREEN'])

# VIP.GREEN  枚举类型

# 枚举的名称和枚举本身不是一个东西.通过名称可以获得枚举类型.

# 枚举的遍历:
for v in VIP:
    print(v)

# VIP.GREEN
# VIP.YELLOW
# VIP.GREEN
# VIP.BLACK
# VIP.RED

# 通过遍历,可以获得枚举类下的每一个枚举类型.