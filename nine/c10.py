"""
9-10
"""


class Student():
    sum = 0  # 一个班级所有学生的总人数

    # 定义构造函数
    def __init__(self, name, age):

        self.name = name
        self.age = age

    # 定义实例方法
    def do_homework(self):
        print('Homework')

    # 定义类方法
    @classmethod # @的形式叫做装饰器
    def plus_sum(cls):
        # 参数列表里有特定名字cls，class的简写
        # 意义和实例列表中的self一样
        cls.sum += 1
        print('当前班级学生总数为：' + str(cls.sum))


student1 = Student('石敢当', 18)
# Student.plus_sum()
student1.plus_sum()
student2 = Student('喜小乐', 18)
Student.plus_sum()


