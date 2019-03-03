"""
13-8 sorted 排序
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

        anchors = []
        for html in root_html:
            name = re.findall(spider.name_pattern, html)
            # refined_name = re.findall(spider.name_refined_pattern, str(name))
            number = re.findall(spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    # 精炼数据
    # 一 主播前后的空格和换行符去掉
    # 二 将字典里的列表转化成单一的字符串的值
    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
            }
        return map(l, anchors)

    # 对抓取下来的数据进行业务排序
    def __sort(self, anchors):
        # anchors = sorted(anchors) 字典不支持sorted()函数
        # key是用来指定字典里哪个元素作为比较大小的元素
        # 指定字典具有可比较性，sorted函数才能生效
        # 如果不指定key函数，sorted认为列表中的元素，字典，进行比较，但是字典不支持小于符号
        # 为key参数编写一个函数
        anchors = sorted(anchors, key=self.__sort__seed, reverse=True)  # reverse=True 降序排列
        return anchors

    # 定义key函数
    def __sort__seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])  # 将string转化为float
        # 将含有万的人数x10000
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展现主播人气排位
    def __show(self, anchors):
        for anchor in anchors:
            print(anchor['name'] + '-----' + anchor['number'])

    # go方法用来总控所有的方法调用
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()

# 排序出现的问题：
# 排序从升序排列改为降序排列
# sorted_seed 直接返回的是字符串不是数字。
# 返回字符串以后，Python按照字符串第一个字符排序。

# sort 函数非常强大
# 自己设计函数的时候能不能想到给别人一个比较开放的函数，让别人来决定用哪一个内容来做排序。
# 学习思想，不仅会用，自己写代码的时候借鉴，自己设计出比较漂亮的函数。

# 现在打印的结果不够漂亮，没有主播排名。下一节课继续完善。

