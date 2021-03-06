"""
13-2 整理爬虫常规思维
"""

# 如何把数据从网页里抓取到我们的程序里。
# 首先知道网页的显示原理
# 我们能够在网页里看到排版规整的文字,是因为网站服务器给了我们一段信息,这段信息是以html格式存在的.
# google浏览器是可以看到具体html.
# F12 Element里显示整个网页相关的html信息.
# 怎么理解左边网页和html之间的关系?
# 浏览器会将html信息翻译成排版规整的网页.
# 找到人数在html里面出现的位置的技巧:
# ctrl+shift+c 用鼠标指在网页上需要抓取的信息左击,右边会自动显示相应的html位置.

# 我们需要收集的信息:
# 主播的名字
# 观看人数

# 很多产品是依靠爬虫所建立的,比如说搜索引擎,今日头条.
# 今日头条会把爬取下来的信息痛过智能筛选，人工分析，深度学习，对它所爬下来的数据进行归纳和整理。
# 爬虫最基本的原理是对于html文件进行文本分析，从而从文本里提取出你要的数据。

# 如何从html里提取信息？
# 正则表达式是最好的处理手段。
# 面对复杂的html结构式文本,python内置的字符串函数很多时候会力不从心.

# 爬虫思路整理
# 爬虫前奏:
# 第一步:明确目的
# 分析某一个游戏主播的排名
# 第二步:找到数据对应的网页
# 第三步:分析网页结构,找到数据所在的标签位置

# 第四步:模拟HTTP请求,向服务器发送这个请求,获取到服务器返回给我们的html
# 通常来说,服务器返回的是一个完整网页的html,这里面数据非常多,并不是每一个数据都是需要的.
# 第五步:我们在拿到html之后,用正则表达式提取我们需要的数据.
# 我们需要主播名字和人气


