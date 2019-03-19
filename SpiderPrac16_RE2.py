'''
正则结果Match的使用案例
'''

import re

# 以下正则分成了两个组，以小括号为单位
s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s, re.I) # s.I表示忽略大小写

m = pattern.match("Hello world wide web")

# goup（0）表示返回匹配成功的整个子串
s = m.group(0)
print(s)

a = m.span(0) # 返回匹配成功的 整个子串的跨度
print(a)

# gourp(1)表示返回的第一个分组匹配成功的子串
s = m.group(1)
print(s)

a = m.span(1) # 返回匹配成功的第一个子串的跨度
print(a)


s = m.groups() #等价于m.gourp(1), m.group(2).......
print(s)


'''
search的使用案例
'''

import re


s = r'\d+'


pattern = re.compile(s)

m = pattern.search("one12two34three56")
print(m.group())


# 参数表明搜查的起始范围
m = pattern.search("one12two34three56", 10, 40)
print(m.group())



'''
findall的使用案例
'''
import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 years odl and 185 high")

print(s)

s = pattern.finditer("i am 18 years odl and 185 high")

print(type(s))

for i in s:
    print(i.group())


'''
中文unicode案例
'''

import re

hello = u'你好，世界'

pattern = re.compile(r'[\u4e00-\u9fa5]+')

m = pattern.findall(hello)
print(m)