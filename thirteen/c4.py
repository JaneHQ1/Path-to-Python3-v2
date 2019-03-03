"""
13-4 HTML 结构分析基本原则二
"""
from urllib import request


class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7r07uci25db'

    # 获取完整网页的html信息
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        # 代码已经跳出了html作用域，没有办法查看它。
        htmls = str(htmls, encoding='utf-8')  # 指定utf-8编码
        # 将bytes转换成string
        a = 1  # 断点放在这里

    # 分析htmls的文档结构
    def __analysis(self):
        pass

    # go方法用来总控所有的方法调用
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()


# 核心的爬虫分析流程
# 第一步：寻找到一个标签或者标识符，这个标识符了可以定位到我们要抓取的信息。
# 学正则表达式的时候我们知道一些常量字符串起到了边界定位的效果。
# 选择哪一个标签作为html的定位标识符？
# 选择标签的三个原则：
# 一 尽量选择有唯一标识性的标签
# 二 尽量寻找最接近我们要提取数据的标签
# 三 在我们选取标签的时候，尽量选取可以闭合的标签。

# 定位标签选得好，正则表达式写得简单，提取的数据会比较精准。

