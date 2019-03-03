"""
13-10 案例总结
"""

'''
This is a module
'''

import re
from urllib import request


class Spider():
    """
     This is a class
    """
    # url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7r07uci25db'
    # url = 'https://www.panda.tv/cate/hearthstone?pdt=1.24.s1.3.7r07uci25db'
    # url = 'https://www.panda.tv/cate/kingglory?pdt=1.24.s1.3.7r07uci25db'
    url = 'https://www.panda.tv/cate/pubg?pdt=1.24.s1.3.7r07uci25db'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    # name_refined_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<i class="ricon ricon-eye"></i>([\s\S]*?)</span>'

    # 获取完整网页的html信息
    def __fetch_content(self):
        """
         This is a class
        """
        r = request.urlopen(Spider.url)

        # This is a comment
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        a = 1
        return htmls

    # 分析htmls的文档结构
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)

        # 建议在这里空一行，阅读感更好
        anchors = []
        for html in root_html:
            name = re.findall(spider.name_pattern, html)
            # refined_name = re.findall(spider.name_refined_pattern, str(name))
            number = re.findall(spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)

        # 建议在这里空一行，阅读感更好
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
        for rank in range(0, len(anchors)):
            # print(anchor['name'] + '-----' + anchor['number'])
            print('rank' + str(rank+1)
                  + ' ' + ':' + ' ' + anchors[rank]['name'] + '  ' + anchors[rank]['number'])

    # go方法用来总控所有的方法调用
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()


# 优化代码：增加主播排名
# 列表的序号就是主播的排名

# 小技巧
# ctrl+f 搜索

# 写函数的技巧：
# go是一个入口方法，也是一个主方法。在主方法里很清晰地展现了数据处理的流程和步骤。
# 推荐多写平级函数，不推荐嵌套函数。

# Python里的注释怎么写？
# Python的注释要写在里面。
# 注释一定要有缩进.
# 推荐在代码上方做单行注释，注释和上一行代码空一行。
# 在Python里善于利用空行。空行最能够增强代码块的概念。
# 注意：
# 不要滥用空行，空行是有意义的，方便大家阅读。
# 最好不要在一个函数里写太多行代码。一个函数里写太多行代码不方便别人阅读。
# 为什么要尽量缩小函数？
# 一 如果函数足够小，函数名就是对函数作用最好的描述，这是缩小函数体积最主要的原因。
# 二 函数体积越小，它就越灵活。复用起来就更方便。
# 行数最好控制在10行到20行，不要超过30行。

# 小技巧
# 熊猫TV的html是按照模板编写的，它的url后面换成别的分类，就可以抓到别的分类的主播排名。

# 这个代码实现了功能，但是写得非常糟糕。
# 它没有把面向对象的思维融入到编程里。
# 这段代码的问题是抵御业务需求变化的能力太差了。
# 如果抓斗鱼直播，整个代码都需要改。
# 可以自己重新架构一个面向对象的代码。

# 中大型爬虫
# 推荐库：Beautiful Soup （用这个库以后，就不用特别依靠正则，它有更简单的方法帮助我们快速地提炼内容。）
# 很多爬虫框架内部集成了Beautiful Soup。
# 如果正则表达式用的很好，根本不需要
# 推荐框架：Scapy
# 小的爬虫不需要框架。
# 框架能不用就不用，研究框架要花费很多时间成本。
# 爬虫最烦人的地方是反反爬虫。
# 爬虫效率
# 爬虫只是过渡技术，更加重要的是把数据爬回来了以后，如何分析提取利用。
# 比如说这个例子，如何精炼数据，以及和业务结合起来如何处理数据。
# 写爬虫的时候最有可能遇到的问题：你当前运行爬虫的服务器可能被封了。
# 就我们这个案例来言，如果不是太频繁地爬取一般情况而言是不会被封的。
# 如果要频繁地更新数据频率要低一点。
# 如果被封了,只能去寻找代理IP.


