# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:45:29 2019

@author: janej
"""

class Student():
    name = '' #不能理解为全局变量。
    age = 0
    
    def __init__(self, name, age): 
        #构造函数
        #初始化对象的特征
        name = name 
        age = age
#        print('student')
    
#    def print_file(self):
#        print('name:' + self.name)
#        print('age:' + str(self.age))
    
    def do_homework():
        print('homework')

#class printer():
#    
#    def print_file(self):
#        print('name:' + self.name)
#        print('age:' + str(self.age))


student1 = Student('石敢当',18)
print(student1.name)
#a = student1.__init__
#print(a)
#print(type(a))

#student2 = Student()
#student3 = Student()

#print(id(student1))
#print(id(student2))
#print(id(student3))