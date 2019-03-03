# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:20:00 2019

@author: janej
"""

class Student():
    #不能理解为全局变量。
    #类变量,不能在这里定义实例变量
    name = 'Jane' 
    age = 0
    sum = 0 #一个班级所有学生的总人数
    
    def __init__(self, name, age): 
        #构造函数
        #初始化对象的特征
        
        self.name = name 
        self.ageggg = age

student1 = Student('石敢当', 18)
student2 = Student('喜小乐', 18)
print(student1.name)
print(student2.name)
print(Student.name )
