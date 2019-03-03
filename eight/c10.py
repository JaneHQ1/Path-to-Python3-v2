"""
8-9 code
"""


# c = 50
# def add(x,y):
#     c = x + y
#     print(c)
#
#
# add(1, 2)
# print(c)


# c = 10
# def demo():
#     print(c)
#
#
# demo()

# def demo():
#     c = 50
#     for i in range(0,9):
#         a = 'a'
#         c += 1
#     print(c)
#     print(a)
#
#
# demo()


c = 1


def func1():
    c = 2

    def func2():
        # c = 3
        print(c)
    func2()


func1()

