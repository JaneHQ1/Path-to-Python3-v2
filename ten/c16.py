"""
10-16 理解Json
"""

# 什么是Json？
# JavaScript Object Notation
# JavaScript 对象标记
# Json 是一种轻量级的数据交换格式。
# Json与另一种交换格式XML相比，Json是相当轻量级。
# Json是一种数据格式。
# 字符串是Json的表现形式。
# 符合Json格式的字符串叫做Json字符串。
# {a: "qiyue" 不是Json字符串，因为不属于Json格式。
# {"name":"qiyue"} 标准Json字符串
# Json字符串很像Python里的字典，因为Json可以和每个语言下的特定数据结构进行转换，所以确实可以变成Python里的字典。
# XML在Json出现以前是主流数据交换格式，大部分互联网服务交换数据都采用XML格式。现在XML使用量越来越少，注重数据结构的领域XML有一定优势。

# Json的优势：
# 易于阅读
# 易于解析
# 网络传输效率高
# 适合做跨语言交换数据
# 如果涉及到用Python调用C++，或者用Java调用.net,更加倾向于把某一种语言所提供的功能做成一个服务，然后利用服务的特性的特性，使用Json传递数据。这样就可以做到跨语言。

# Json应用场景
# 网站后台 -> 浏览器
# 我们通常看到的网页就是网站后台向浏览器传输的html。
# Json和html一样，也是一串数据。
# 浏览器就是为html量身定做的，它可以把html的标记性语言显示成我们看到的样式。
# 这几年Ajax技术出现以后，我们越来越多地从浏览器里发送请求，获取Json数据。浏览器拿到Json数据以后，它可以在前端做一些逻辑运算，最终把Json数据呈现给大家。
# html很多时候并不适合移动端的应用，Json的优势是可以跨不同的语言，各个服务之间也存在数据的传输， 如果我们都可以使用Json数据格式传输，就不需要考虑我们具体使用什么语言来实现的/
# 比如说API服务用Java写的，我们用Json可以很容易的和API服务Python做数据的交互。
# 单页面一般用Javascript做，网站后台和Javascript也可以用Json传输。

# Summary
# Json只是一个数据格式，是为了做数据交换而制定的数据规范。Json字符串是它的载体。
# Json是跨语言的，并不是某一个语言所特有的。
