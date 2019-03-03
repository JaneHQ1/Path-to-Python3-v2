"""
9-7
"""


class Student():
    # 不能理解为全局变量。
    # 类变量,不能在这里定义实例变量
    name = 'Jane'
    age = 0
    sum = 0  # 一个班级所有学生的总人数

    # 构造函数（可以看作特殊的实例方法）
    # 初始化对象的属性
    def __init__(self, name, age):

        self.name = name
        self.age = age
        # print(name)  # 读取的是形参name
        print(self.name)  #读取的是对象name
        print(Student.sum)
        print(self.__class__.sum)

    def do_homework(self):
        print('homework')


student1 = Student('石敢当', 18)

# student1.do_homework()
# print(Student.__dict__)
# print(student1.__dict__)
# print(student1.name)
# print(Student.name)

