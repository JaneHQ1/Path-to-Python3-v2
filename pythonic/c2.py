'''
    14-2 用字典映射代替switch case语句
'''

# 在Python中如何巧妙地利用字典的特性去代替其他语言里的switch?
# C#里的switch例子:
'''
switch(day)
{
case 0:
    dayName = "Sunday";
    break;
case 1:
    dayName = "Monday";
    break;
case 2:
    dayName = "Tuesday";
    break;
...
default:
    dayName = "Unknown";
    break;
'''

# switch是条件分支语句.
# switch语句后面接收一个变量,它的case就是当变量取某一个值得时候,执行哪一个代码块.
# 如果变量不是case中得任意一个得时候,执行default的默认语句.

# if else可以代替switch,但是个人觉得不合适.
# 如果if else可以代替switch,那其他语言也没必要怎加switch条件分支语句,直接用if else.
# 我们可以使用字典的映射代替switch语句.

"""
switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
}


day = 0
date = switcher[day]
print(date)
"""

# Sunday

# 执行和switch一样,但是怎样模拟default分支?
# 用get方法访问
# get方法具有容错性
# 如果用get方法访问,即使key不存在也不会报错,它会返回默认值.

"""
day = 6
date = switcher.get(day, 'Unknown')
print(date)
"""

# case语句下面可以写完整的代码块,但是字典最多只能写一个lambda表达式
# 可以利用函数式编程的特性.
# key对应的value不仅仅是字符串,还可以对应一个函数,这和把函数赋值给变量是一个道理.


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unknown'


switcher = {

    # 这里千万不能加()
    # 加了括号得到的是string，和之前的switcher没有什么区别
    # 0: get_sunday(),
    # 1: get_monday(),
    # 2: get_tuesday(),

    0: get_sunday,
    1: get_monday,
    2: get_tuesday,
}

day = 0
date = switcher.get(day, get_default)()
print(date)

# 如果key在字典里不存在,那这样的写法会报错.因为如果没有key,返回的就是个字符串,字符串后面加括号没有意义.
# 默认值也定义函数,这样字典也可以兼容默认值的情况.
# 写业务的时候函数里可以写很多逻辑.
# 现在字典映射就完美地替换了别的语言的switch。
