# -*- coding: utf-8 -*-
"""
9-14 code

@author: janej
"""

# 建议一个模块一个类  
# 如何让Student（c13）Human(c14)?
class Human():
    sum = 0
    def __init__(self, name, age):

        self.name = name
        self.age = age
    
    def get_name(self):
        print(self.name)
        
    def do_homework(self):
        # 子类方法可以和父类同名
        print('This is a parent method')
        

