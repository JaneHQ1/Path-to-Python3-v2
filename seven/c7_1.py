"""
    7-1 while循环使用场景
"""
# 循环
# 循环不仅仅是Python里的一个语法，更应该是我们解决问题的思维模式。
# 计算机通过循环和穷举的方式解决复杂问题。
# 高强度循环的利用:
# 密码破解方法：暴力破解， 穷举所有字母和字符的组合，尝试比对一个正确的结果。

# Python使用循环语句构建循环思想.
# 常见的两种循环语句:
# for 循环
# while 循环

# while 循环:
# while condition:
#   代码块

'''
CONDITION = True

while CONDITION:
    print('I am while')
    
# 无限死循环
'''
# while 非常容易造成无限死循环

# while 的机制:
# 如果CONDITION是True,执行下面的代码块.
# 执行以后会再一次检测CONDITION, 如果CONDITION依然是True, 它还会继续执行代码块.
# CONDITIOND 的状态永远是True，它会一直循环。

# while的正确用法：
counter = 0

while counter <= 3:
    print(counter)
    counter += 1
else:
    # 在结束程序前时候打印结束标式
    print('EOF')

# 0
# 1
# 2
# 3
# EOF

# 如何避免while的死循环？
# while的条件判断语句不应该是一个常量。
# 如果是一个常量，它的条件判断结果是永远不会改变的。
# 如果希望while的运行次数有限，在while的内部代码块里就必须要有能够影响条件判断的语句。
# 比如说上面的例子，在代码块里counter + 1 就是影响条件判断的语句。
# while 还可以和else一起使用。
# while 后面的条件语句是False的时候，执行else分支后面的代码块。
# 类比if else

# while 和 for 的使用场景可以形象地比喻
# while使用场景：
# 给自己设定目标，达到目标后停止，执行else中的命令。
# 递归 recursion 使用while非常合适，其他运用场景建议使用for。

