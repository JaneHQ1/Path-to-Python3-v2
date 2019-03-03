"""
13-5 数据提取层级分析及原则三
"""

# 按照上节课的两个原则寻找定位标签。
# 主播名：
# <span class="video-nickname" title="LOL卷子">
# 观看人数：
# <span class="video-number"><i class="ricon ricon-eye"></i>2.3万</span>
# 肉眼可以看出标签是否靠近提取信息。

# 怎样确认唯一性？
# 可以利用正则表达式验证

# 不建议直接对我们找到的两个标签分别做正则分析。
# 假如说先对video-nickname做正则分析，可以得到一组主播的姓名。
# 接着对video-number分析，可以得到一组人气数据。
# 但是问题在于这两组数据如何对应起来。所以分别做正则分析不是太方便。
# 靠序号匹配不保险，网页很多时候是未知的。如果网页是规律的，也许匹配是正确的。如果网页不规律，很有可能匹配的是错的。
# 如何解决？
# 可以把两个数据当作一组数据，在这组数据外面再找一个标签，离这组数据最近，并且也有唯一性。
# <div class="video-info">
# 第三个原则：在我们选取标签的时候，尽量选取可以闭合的标签。
# 什么叫做可以闭合的标签？
# <div class="video-info">
#           <span class="video-title" title="老卷儿—打野教科书！">老卷儿—打野教科书！</span>
#                     <span class="video-nickname" title="LOL卷子">
#                                     <i class="icon-hostlevel icon-hostlevel-10" data-level="10"></i>
#                                     LOL卷子          </span>
#                     <span class="video-number"><i class="ricon ricon-eye"></i>2.3万</span>
#                     <span class="video-station-info">
#             <i class="ricon ricon-fleet"></i>
#             <i class="video-station-num">47人</i>
#                         </span>
#                   </div>
# 这个div标签有一个开头和一个结尾，刚好可以把的video-nickname和vieo-number包裹起来。这就叫闭合标签
# # 我们尽量选择这样的标签。
# 这也是为什么不选video-title做标签，因为这个标签没有把video-nickname和vieo-number包裹起来。
# 尽量选择父级标签，video-title属于兄弟级别标签，不太适合做为定位标签。
# 用兄弟标签做定位标签也可以，但是正则表达写得会比较复杂。
# video-nickname和vieo-number也是闭合标签。

# 我们选择的三个标签：
# <div class="video-info">
# 闭合div标签，包含两个闭合标签：
# <span class="video-nickname" title="LOL卷子">
# span标签，包含我们要抓取的主播姓名信息。
# <span class="video-number"><i class="ricon ricon-eye"></i>2.3万</span>
# span标签，包含我们要抓取的主播人气信息。

# 标签结构理清楚以后，正则表达式的编写思路写浮出水面。
# 一 利用video-info标签缩小html匹配范围，拿到video-info标签内部的内容。
# 二 用正正则表达式匹配video-info内部的内容，进一步找到video-nickname和vieo-number。
# 三 再利用video-nickname标签进一步寻找它内部的数据。最终找到我们要的数据。

# 这里是三级文档，提取两次就可以提取出来了。
# 不规范的网页要提取更多次，但是提取流程不变，都是数据精细化的过程。

# 爬虫最麻烦的是爬虫和反爬的较量。

# 我们通过一个正则表达式提取出一组video-info，然后通过循环分别在每一个video-info里面提取video-nickname和video-number。

