'''
    7-2 for与for-else循环
'''

# for 循环
# for target_list in expression_list:
#     pass
# 自己定义target_list， 可以定义符合Python变量规则的变量
# expression_list 代表一个列表

# for 和 while 在使用场景上有什么不同？
# 主要是用来遍历/循环序列或者集合，字典。
# 凡是表示组概念的，Python都可以使用for循环来遍历。
# 遍历非常能够体现for循环特性。

a = ['apple', 'orange', 'banana', 'grape']
# for x in a:
#     print(x)

# apple
# orange
# banana
# grape

# x代表列表里的某一个元素。
# 当循环遍历到apple，x就是apple。

# 代码块内部还可以嵌套代码块：

a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
# 打印出列表里所有的元素
# for x in a:
#     print(x)

# ['apple', 'orange', 'banana', 'grape']
# (1, 2, 3)


# 把所有列表打印出来了

# 如何把子列表所有元素打印出来？
# for x in a:
#     for y in x:
#         # print(y)
#         # 将每一个元素放在一行
#         # 不设置end的值，默认\n
#         print(y, end=' ')

# apple
# orange
# banana
# grape
# 1
# 2
# 3

# 列表元素纵向打印出来

# apple orange banana grape 1 2 3

# 列表元素横向打印出来


# for-else：当列表中所有的元素都遍历完了，就执行else中的内容。
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
# for x in a:
#     for y in x:
#         print(y)
# else:
#     print('No fruits')

# grape
# apple
# orange
# banana
# grape
# 1
# 2
# 3
# No fruits

# 当所有列表元素被遍历打印出来之后，最后'No fruits'被打印出来了。

# for else 有条件判断， for else没有。
# 对for else来说，else什么时候执行？
# 当列表里所有的元素都遍历完以后，else里的内容开始执行。

# 终端循环：
a = [1, 2, 3]
# for x in a:
#     if x == 2:
#         break
#     print(x)

# 1

# for loop中间遇到break，循环立刻结束，不会继续break后面的代码，包括后面的循环。

# 跳过x=2，依然打印x=3,怎么半？
# for x in a:
#     if x==2:
#         continue
#     print(x)

# 1
# 3

# for loop中间遇continue，跳过当前步骤，后面循环继续。

# break:强行终止当前循环,并且以后的循环都不会继续
# continuous: 终止当前循环,后续循环继续执行

# for x in a:
#     if x == 2:
#         break
#     print(x)
# else:
#     print('EOF')

# 1

# 不会执行else语句
# 如果for循环不是正常结束,强制break打断是不会执行else语句.这是一个很大的误区.

# for x in a:
#     if x == 2:
#         continue
#     print(x)
# else:
#     print('EOF')

# 1
# 3
# EOF

# 用continue任然遍历完了,还是会打印出'EOF'


a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':
            break
        print(y)
else:
    print('No fruits')

# apple
# 1
# 2
# 3
# No fruits

# 加入break之后,为什么else任然可以执行?
# 从orange打断,为什么后面的1,2,3任然被打印出来?


