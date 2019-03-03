"""
13-7 正则获取名字和人数
"""
# 在之前的匹配结果里继续匹配。
# <span class="video-title" title="LPL春季赛LGD vs FPX">LPL春季赛LGD vs FPX</span>
#                     <span class="video-nickname" title="LPL熊猫官方直播">
#                                     <i class="icon-hostlevel icon-hostlevel-vip"></i>
#                                     LPL熊猫官方直播          </span>
#                     <span class="video-number"><i class="ricon ricon-eye"></i>70.6万</span>
#                     <span class="video-station-info">
#             <i class="ricon ricon-fleet"></i>
#             <i class="video-station-num">17人</i>
#                         </span>

import re
from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7r07uci25db'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
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
            number = re.findall(spider.number_pattern, html)
            anchor = {'name': name, 'number': number}  # 将name和number平成一个字典
            anchors.append(anchor)  # 在列表anchors添加一个元素anchor
        #     遍历完成以后，anchors里包含所有主播名字和人气的字典。
        print(anchors[0])
        print(anchors[1])
        return anchors

    # 精炼数据
    def __refine(self, anchors):
        pass

    # go方法用来总控所有的方法调用
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__refine(anchors)



spider = Spider()
spider.go()
