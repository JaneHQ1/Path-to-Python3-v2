"""
9-12
"""


class Student():

    sum = 0  # 一个班级所有学生的总人数

    # 定义构造函数
    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.__score = 0

    # def __init__(self, name, age, score):
    #
    #     self.name = name
    #     self.age = age
    #     self.score = score
    #     print(self.name + '同学本次考试分数为：' + str(self.score))

    def marking(self, score):
        self.__score = score
        print(self.name + '同学本次考试分数为：'+ str(self.__score))

    # 定义实例方法
    # def do_homework(self):
    #     # 在类的内部调用另外一个函数
    #     self.do_english_homework()
    #     print('Homework')

    # def do_english_homework(self):
    #     print('English Homework')

    # 定义类方法
    # @classmethod # @的形式叫做装饰器
    # def plus_sum(cls):
    #     # 参数列表里有特定名字cls，class的简写
    #     # 意义和实例列表中的self一样
    #     cls.sum += 1
    #     print('当前班级学生总数为：' + str(cls.sum))
    #
    # # 定义静态方法
    # @staticmethod
    # def add(x, y):
    #     print(Student.sum)
    #     print(name)
    #     print('This is a static method')


# student1 = Student('石敢当', 18, 59)
# student1.do_homework()  # 在类外部调用方法
student1 = Student('石敢当', 18)
result = student1.marking(59)
student1.__score = -1
print(student1.__score)
# print(student1.name + '同学本次考试分数为：' + str(student1.score))
