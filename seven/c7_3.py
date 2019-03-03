"""
    7-3 for与range
"""

# a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
# for x in a:
#     for y in x:
#         if y == 'orange':
#             break
#         print(y)
# else:
#     print('No fruits')

# apple
# 1
# 2
# 3
# No fruits

# 加入break之后,为什么else任然可以执行?
# break跳出的是内循环,但是else配对的是外循环.跳出内循环并没有跳出外循环,所以else依然会执行.

# 从orange打断,为什么后面的1,2,3任然被打印出来?
# 最根本的原因是因为这里有两个嵌套的循环,break跳出的是内部的循环,内部循环跳出以后,外部循环还在进行.
# 第一个列表里orange之后的元素都不会打印,因为他们的循环已经跳出.
# 多维度循环非常容易出错的地方.

# for循环设计的初衷是用来遍历列表.
# 其他语言的 for(i=0, i<10, i++)如何在Python里表示?
# 如何在Python里指定重复次数?
# 让一段代码执行10次:
# for x in range(0, 10):
#     print(x)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# range函数可以按照我们指定的规则生成一个序列.
# range(0, 10)生成了一个从0到数字9的序列
# 0表示起始数字.
# 10表示的不是终止数，而是偏移量。
# 从0开始，总共10个数字。

# 如何生成有间隔的序列2,4,6,8?
# for x in range(0, 10, 2):
#     print(x)

# 0
# 2
# 4
# 6
# 8

# 第三个参数是间隔

# 递增等差数列
# for x in range(0, 10, 2):
#     print(x, end=' | ')

# 0 | 2 | 4 | 6 | 8 |

# 递减等差数列:
for x in range(10, 0, -2):
    print(x, end=' | ')

# 10 | 8 | 6 | 4 | 2 |

# range函数非常强大,善于用range函数生成序列.