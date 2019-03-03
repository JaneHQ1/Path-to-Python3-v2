"""
8-7 code
"""


# def demo(*param):
#     print(param)
#     print(type(param))
#
#
# demo(1,2,3,4,5,6)


# def demo(*param):
#     print(param)
#     print(type(param))
#
#
# a = (1,2,3,4,5,6,)
# demo(*a)


# def demo(param1, *param, param2=2):
#     print(param1)
#     print(param)
#     print(param2)
#
#
# demo('a', 1, 2, 3, 'param')


def demo(param1, param2=2, *param):
    print(param1)
    print(param2)
    print(param)


demo('a', 1, 2, 3)