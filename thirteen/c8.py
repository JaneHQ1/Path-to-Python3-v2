"""
13-8 数据精炼
"""

import re
from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7r07uci25db'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    # name_refined_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<i class="ricon ricon-eye"></i>([\s\S]*?)</span>'

    # 获取完整网页的html信息
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        a = 1
        return htmls

    # 分析htmls的文档结构
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)

        anchors = []  # 定义anchors列表
        for html in root_html:
            name = re.findall(spider.name_pattern, html)
            # refined_name = re.findall(spider.name_refined_pattern, str(name))
            number = re.findall(spider.number_pattern, html)
            anchor = {'name': name, 'number': number}  # 将name和number平成一个字典
            anchors.append(anchor)  # 在列表anchors添加一个元素anchor
        #     遍历完成以后，anchors里包含所有主播名字和人气的字典。
        # print(anchors[0])
        # print(anchors[1])
        return anchors

    # 精炼数据
    # 一 主播前后的空格和换行符去掉
    # 二 将字典里的列表转化成单一的字符串的值
    def __refine(self, anchors):
        # 保留字典格式
        # 字典里的值是一个列表
        # 列表只有一个元素
        # 列表里的元素是字符串
        # 内置函数strip()去除前后的换行符以及空格
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
            }
        return map(l, anchors)

    # go方法用来总控所有的方法调用
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        print(anchors)

    # 对抓取下来的数据进行业务排序
    def __sort(self, anchors):
        pass



spider = Spider()
spider.go()

# 要去除字符串前后的空格，先考虑Python是否有内置函数可以处理这个问题，不要想着用loop或正则解决。

# 精炼数据和html提取数据有什么不同？
# 提取数据主要是分析html的结构。
# 我们获得数据以后，由于数据不太规范，所以我们需要通过精炼的过程把数据进一步规范成我们要的数据结构。

# 下一步是业务处理
# 我们要对所抓取下来的数据进行业务排序。

