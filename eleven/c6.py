"""
11-6 枚举转换
"""
from enum import Enum

# 编写服务器代码的时候需要和数据库打交道。一般情况下村，想在数据库里存储枚举值通常在数据库里存储枚举的具体数字。
# 除了在数据库里存储数值用来代表枚举之外，还可以选择存储标签名字，将标签名字以字符串的形式存到数据库里某一个字段里表示枚举类型。
# 建议使用数值来存储枚举类型，不建议用字符串的形式。因为数字更加简洁，占用数据库的空间更小。
# 但是不建议在代码里用数字代表枚举类型。
# 最好在代码里显示定义一个枚举类，用枚举类下的枚举类型定义数据库里的每一个数值。在编写代码的时候用枚举类的可读性更强一点。
# 代码最重要的是可读性。

# 如果从数据库里查询到数字，如何将数字转化成枚举类型？

class VIP(Enum):
    YELLOW = 1
    GREEN = 1  # YELLOW_ALIAS = 1
    BLACK = 3
    RED = 4


a = 1  # 假设从数据库得到数字1
print(VIP(a))

# VIP.YELLOW

# 使用数值访问枚举类型的方案，我们可以看作是一个类型转换，但实际上并不是一个真正的类型转换。


