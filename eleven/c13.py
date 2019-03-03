"""
11-13 出个题，用闭包解决！
"""

# 闭包有什么用？
# 它很像枚举，它可以帮助我们精简代码，让代码架构更加合理。
# 闭包只是思维方式的不同
# 很多公司面试都会问闭包的概念。

# 练习题
# 计算旅行者路径的长度：
# 二维里决定地标是 x,y
# 我们简化成一维 x
# x =0 代表起点
# 每走一步加1
# 编写一个函数，通过不断调用这个函数得到旅行者当前所处的位置。



def cal_distance(move):
        start_point = 0
        move_steps = move
        def acc_distance():
            new_location = start_point + move_steps
            return new_location
        start_point = acc_distance()
        print('Your current location is ' + str(start_point))
        return acc_distance

x = cal_distance(2)
x = cal_distance(5)
x = cal_distance(11)
# print(x.__closure__)

# Your current location is 2
# Your current location is 5
# Your current location is 11

# start_point 不应该放在函数里面. 要不 starting_point 不会变.

start_point = 0

def cal_distance(location):
    def acc_distance(move):
        nonlocal location
        new_location = location + move
        location = new_location  # 闭包的环境变量有保存现场的功能, 它可以记忆上一次调用的状态.
        return new_location
    return acc_distance

x = cal_distance(start_point)
print(x(2))
print(x(5))
print(x(11))