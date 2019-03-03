"""
13-6 正则分析
"""
import re
from urllib import request


class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7r07uci25db'
    # root_pattern = '<div class="video-info">[\s\S]*?</div>'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'  # 加入组括号
    # 注意："video-info" 的双引号是必须的，因为在我们匹配的原始的html里面是有这个双引
    # 我们巧妙地运用地Python地单双引号地特性。外部单引号表示Python的字符串。
    # 外面使用双引号，里面使用单引号就匹配不到了。
    # 只写定位标签无法匹配到任何内容,因为我们我们要匹配的的不是<div class="video-info">，要匹配的是它中间的所有内容。
    # []里是或的关系
    # * 匹配0次或者无限多次
    # 只想获取两个div标签内部的内容,需要选取非贪婪模式.
    # 默认贪婪模式会发生什么?
    # /div会有很多个,如果默认贪婪模式,我们无法精准定位一个video-info内部的信息.

    # 获取完整网页的html信息
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        # 代码已经跳出了html作用域，没有办法查看它。
        htmls = str(htmls, encoding='utf-8')  # 指定utf-8编码
        # 将bytes转换成string
        a = 1  # 断点放在这里
        return htmls

    # 分析htmls的文档结构
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        print(root_html[0])
        print(root_html[1])
        print(root_html[2])
        a = 1

    # go方法用来总控所有的方法调用
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()

# TypeError: expected string or bytes-like object

# 我们可以调试,查看哪里出错了.
# 在go方法里 html = {NoneType}None
# 我们可以判断__fetch__content里没有返回htmls的值.

# <div class="video-info">
#           <span class="video-title" title="LPL春季赛LGD vs FPX">LPL春季赛LGD vs FPX</span>
#                     <span class="video-nickname" title="LPL熊猫官方直播">
#                                     <i class="icon-hostlevel icon-hostlevel-vip"></i>
#                                     LPL熊猫官方直播          </span>
#                     <span class="video-number"><i class="ricon ricon-eye"></i>37.9万</span>
#                     <span class="video-station-info">
#             <i class="ricon ricon-fleet"></i>
#             <i class="video-station-num">17人</i>
#                         </span>
#                   </div>

# 定界标签<div class="video-info"></div>也包含在匹配结果里.
# 有没有可能去掉标签,只保留中间内容?
# 可以利用组的概念.中间的内容用圆括号括起来.

# <span class="video-title" title="LPL春季赛LGD vs FPX">LPL春季赛LGD vs FPX</span>
#                     <span class="video-nickname" title="LPL熊猫官方直播">
#                                     <i class="icon-hostlevel icon-hostlevel-vip"></i>
#                                     LPL熊猫官方直播          </span>
#                     <span class="video-number"><i class="ricon ricon-eye"></i>70.6万</span>
#                     <span class="video-station-info">
#             <i class="ricon ricon-fleet"></i>
#             <i class="video-station-num">17人</i>
#                         </span>

# 结果里没有了定界标签<div class="video-info"></div>.

# 常用概括字符集有三种:
# \d \D
# 单词字符集：\w \W
# 单词字符集范围：[A-Za-z0-9_]
# 空白字符集：\s \S
# 空白字符集例子：[' ', '\t', '\n', '\r']
# . 匹配除换行符之外其他字符
# Note:'&'不属于单词字符集和空白字符集
# * 匹配0次或者无限多次

# 思考:
# 如果我们将[\s\S]改成[.],为什么匹配不出来?
# root_pattern = '<div class="video-info">[\s\S]*?</div>'
