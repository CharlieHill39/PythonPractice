'''
安装lxml
'''
from lxml import etree

'''
用lxml来解析HTML代码
'''

text = '''
<div>
    <ul>
        <li class="item-0"> <a href="0.html"> first item </a></li>
        <li class="item-1"> <a href="1.html"> first item </a></li>
        <li class="item-2"> <a href="2.html"> first item </a></li>
        <li class="item-3"> <a href="3.html"> first item </a></li>
        <li class="item-4"> <a href="4.html"> first item </a></li>
        <li class="item-5"> <a href="5.html"> first item </a>
    </ul>
</div>
'''

# 利用etree.HTML把字符串解析成HTML文档并可以给它补全
html = etree.HTML(text)
s = etree.tostring(html)
print(type(s))
print(s)

'''
etree与xpath综合运用
'''
from lxml import etree

# 只能读取xml格式内容，html报错
html = etree.parse("./v30.html")

rst = etree.tostring(html, pretty_print=True)
print(rst)

rst = html.xpath('//book')
print(type(rst))
print(rst)

# xpath的意思是，查找带有category属性值为sport的book元素
rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

# xpath的意思是，查找带有category属性值为sport的book元素下的year元素
rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)