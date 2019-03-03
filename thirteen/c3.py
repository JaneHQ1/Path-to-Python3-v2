"""
13-3 调试代码
"""
from urllib import request
# 通过request对象获取html网页


class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7r07uci25db'

    # 获取完整网页的html信息
    # 将fetch_content设置为私有方法
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        # print(htmls)

    # go方法是Spider的入口方法
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()

# print调试方法非常不好，不推荐在逻辑性比较强的代码里print。因为用print以后到处都是print，而且print只能看到一个变量，过程中的变量看不到。
# 如果想看过程中的所有变量，要加入很多print。把每个变量都打印出来。
# 推荐断点调试
# 调试的重要性
# print，单元测试都是调试。
# 断电调式是每一个开发者必须掌握的技能。
# 培养独立思考和解决问题的能力是终身受益的事情。

# 快捷键
# Alt + Shift + F9 调试模式配置
# F8 跳过
# F7 进入
# Shift + F8 退出
# Alt + F9 运行游标 （Run to Cursor）运行以后就可以看变量的状态了。
# Alt + F8 验证表达式
# Ctrl + Alt + F8 快速验证表达式
# F9 恢复程序
# Ctrl + F8 断点开关
# Ctrl + Shift + F8 查看断点

# 断点调试有什么作用？
# 可以观察变量的状态以及相应的属性和取值。