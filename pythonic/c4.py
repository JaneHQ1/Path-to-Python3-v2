'''
    14-4 字典如何编写列表推导式
'''

# 字典的列表推导式

student = {
    '喜小乐': 18,
    '石敢当': 20,
    '横小五': 15

}

# 将key提取出来，组成为一个列表
# 遍历一个列表或者元组只需要一个形参，但是对于字典要有两个，key和value
"""
b = [key for key, value in student]
print(b)

# ValueError: too many values to unpack (expected 2)
"""
# student字典不能被for in， 要调用字典item方法
b = [key for key, value in student.items()]
print(b)

# ['喜小乐', '石敢当', '横小五']


# 将student字典的key和value颠倒
b = {value:key for key, value in student.items()}
print(b)

# {18: '喜小乐', 20: '石敢当', 15: '横小五'}


# 将dict改为元组
b = (key for key, value in student.items())
print(b)

# <generator object <genexpr> at 0x00000151AA642480>

# 得到的是generator,无法直接将元组打印出来,因为它打印出来的不是元组,而是可遍历的对象generator.